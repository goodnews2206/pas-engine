# PAS303 — Agent Cockpit Product Spec

> Status: product direction document (planning only — no UI, frontend, backend, auth, CORS, or package changes).
> Owner: ORVN Labs.
> Anchored on: `main` @ `8e9b237`, with PAS301, PAS301.5, and PAS302 authored on branch `pas301-identity-ownership-session-workspace-lifecycle`.
> Defines: the Agent Cockpit — the daily operating surface at the center of PAS. The product the entire distribution thesis rests on.
> Naming: **PAS = Proactive Assistant for Scale.**
> Reading note: this is written as a product philosophy that happens to define a surface — not a requirements list. Every section is an argument, not a backlog.

---

## 1. Executive summary

This is the most important thing PAS has to get right. PAS300 set the direction, PAS301 made
identity and ownership safe, PAS301.5 chose how people get in, and PAS302 established that the
agent is the center of gravity. PAS303 is where all of that either becomes real or stays a deck:
**the actual screen an agent opens before they open anything else.**

The Agent Cockpit exists to answer one question, every morning, before the agent has finished
their coffee: *what matters today?* It becomes the primary landing experience for agents
(PAS302 §8) because the agent's first need is never "show me everything" — it is "tell me what
to do." A product that meets that need at 7:00 a.m. earns the most valuable real estate in
software: the first tab.

**Dashboards fail** because they are passive. A dashboard is a room full of dials; it waits for
you to walk in, read them, interpret them, and decide what to do. It assumes you arrive with a
question. But an agent at the start of the day doesn't arrive with a question — they arrive with
dread (what did I drop?) and scarcity (what's the highest-value thing I could touch?). A
dashboard answers neither. It describes a business; it does not run a day. That is why
dashboards get opened on Mondays and abandoned by Thursday.

**Daily operating companions win** because they are active. A companion has already looked at
everything overnight, formed a point of view, and greets you with it. It doesn't ask you to
interpret — it tells you what changed, what's at risk, and what to do first, and it's usually
right. The difference between a dashboard and a companion is the difference between a tool you
check and a colleague you trust. PAS303 is the spec for the colleague.

If PAS303 fails, PAS fails — there is no enterprise sale to a brokerage whose agents won't open
the product. If PAS303 succeeds, agent adoption becomes possible, and everything else PAS300
described becomes reachable.

---

## 2. The core job

The Agent Cockpit is **not** a CRM, not a task manager, not a dashboard, not a reporting screen.
Each of those is a place you go to *look something up* or *file something away* — destinations
that put the work on you. The cockpit's job is the opposite.

> **The Agent Cockpit's single job is to turn the agent's entire scattered operation into one
> confident answer to "what should I do right now" — and to keep that answer true all day.**

Everything else the cockpit shows is in service of that one job. It is not a place to store
data; it is a place that has already read the data and decided what it means for *you, today*.
The agent should never have to assemble the answer themselves by reading five panels — the
cockpit assembles it and hands it over. The measure of the cockpit is not how much it displays;
it is how little the agent has to think before they know what to do.

A CRM remembers. A task manager lists. A dashboard reports. The cockpit **decides what's
next** — and that verb is what makes it a companion rather than a tool.

---

## 3. The morning-open test

The only test that matters. An agent wakes up. Their phone has Gmail, their CRM app, and a wall
of unread texts. Why do they open PAS *first* — before any of those?

Because the other three give them **raw material**, and PAS gives them **a plan**. Gmail is a
pile of inputs. The CRM is a filing cabinet. Texts are noise with a few signals buried in them.
Opening any of them at 7 a.m. starts the day with *sorting* — the exact cognitive load the agent
dreads. Opening PAS starts the day with *clarity*: PAS has already read across all of it
overnight and distilled it.

When the agent opens PAS in the morning, they should immediately receive **the shape of their
day in one glance**: the few things that genuinely need them, the things quietly slipping, the
one or two opportunities worth their energy, and the single best first move.

What PAS should **already know** by the time they open it: who went cold overnight, which
callbacks come due today, which deals didn't move, what they promised someone last week and
haven't done, and what changed since they closed the laptop. The agent should never have to tell
PAS what happened — PAS should be telling *them*.

What PAS should **proactively surface**: not everything that happened, but everything that
*matters* — filtered hard, ranked by consequence, and framed as action. The morning open is not
a feed; it is a briefing. The test is passed the day the agent reaches for PAS instinctively,
the way they reach for coffee — not because they were told to, but because it's the fastest path
to feeling in control of the day.

---

## 4. Emotional outcome

The cockpit is judged on a feeling, not a feature count. Productivity-app language —
"dashboards," "widgets," "metrics," "engagement" — is the wrong vocabulary, because it describes
software, not the human using it. The cockpit must produce four emotions, in this order:

- **Relief.** The first half-second has to dissolve the background dread of "what am I
  forgetting?" PAS has it. Nothing is silently rotting. The agent can exhale.
- **Confidence.** What's in front of them is *the right things* — not a comprehensive list they
  have to triage, but a trustworthy short list they can act on without second-guessing.
- **Clarity.** They know exactly what to do next. No interpretation, no deciding-what-to-decide.
  The fog is gone.
- **Momentum.** The first action is obvious and doable, so they start — and starting is the
  whole game. A morning that begins with one clear action becomes a day with motion.

Relief → confidence → clarity → momentum is the emotional arc of every morning open. If the
cockpit produces anxiety (too much), doubt (unclear), or paralysis (too many choices), it has
failed regardless of how much it shows. The cockpit's true output is *an agent who feels on top
of their day* — the screen is just how that feeling gets delivered.

---

## 5. First screen

What appears above the fold is the entire product decision compressed into one view. The first
screen must lead with **a point of view, not a layout.**

The first thing PAS says every morning is a single human sentence — the briefing's headline —
something like *"Three things need you this morning, and the Hendersons are going cold."* Not a
greeting, not a metric, not a grid. A sentence that tells the agent what their day is about
before they've scrolled.

**Deserves first attention:** the one-to-three things that genuinely need the agent, and the
single most valuable next action. The agent should be able to *act* from the first screen, not
just read it.

**Should never appear first:** comprehensive lists, full pipelines, raw counts, charts, "total
leads: 247," settings, or anything that asks the agent to interpret rather than act. The full
operation is available — one layer down, on demand — but it is never the opening move. The first
screen is the cockpit's thesis statement: *PAS already thought about your day so you don't have
to start from zero.* Everything that violates that thesis belongs below the fold or behind a
click.

---

## 6. The Daily Brief

The Daily Brief is, very likely, the most important component in all of PAS. It is the cockpit's
voice — the thing that makes PAS feel like a companion with a point of view rather than a screen
of data. If the Daily Brief is good, the agent opens PAS forever. If it's noise, nothing else
matters.

**What's in it:** the shape of the day, in priority order — what needs them, what's slipping,
what's worth doing, and the first move. It reads like the briefing a great chief of staff gives
you in the hallway: short, specific, prioritized, and *opinionated*. It names names ("the
Hendersons," "your 2 p.m. callback to Maria"), not categories ("3 leads require attention"). It
tells the agent what *changed* since yesterday, because change is what a briefing is for.

**What's not in it:** everything that isn't consequential today. No exhaustive lists, no metrics
for their own sake, no "here's your whole pipeline," no recap of things already handled. The
brief earns its trust by being ruthlessly edited. A brief that includes everything is just a
feed, and feeds are ignored.

**How long to read:** under a minute. Thirty seconds is the target. If reading the brief feels
like work, it has failed — the brief exists to *remove* work, not add a reading assignment. Its
job is to be the fastest possible path from "I just woke up" to "I know what to do."

**How personalized:** completely. The brief is written *for this agent, about their book, in a
voice they've configured* (PAS304 — the name they gave PAS, the tone they chose). It is not a
template with variables; it is PAS having looked at *their* world and telling *them* about it.
The personalization is the product. A generic brief is a newsletter; a personal brief is a
relationship.

---

## 7. "What needs me"

A dedicated section, governed by a single discipline: it contains **only things that genuinely
require a human** — the agent specifically. Not everything. Not "everything assigned to you."
Only the decisions and actions that cannot happen without the agent's judgment, voice, or
authority.

The philosophy: **attention is the agent's scarcest asset, and PAS's job is to protect it.**
Most software competes for attention; PAS competes to *return* it. Every item that appears in
"What needs me" is an item PAS has decided it cannot handle alone — a real client conversation,
a judgment call, an approval, a relationship moment. Everything PAS *can* handle is deliberately
*not* here (it's in §8). The smaller this list is, the more PAS is working; a long "What needs
me" list means PAS is failing to carry its share.

This inversion — showing less, not more — is what separates the cockpit from a task manager. A
task manager shows you everything you owe. The cockpit shows you only what *only you* can do, and
quietly takes the rest off your plate.

---

## 8. "What PAS can handle"

The counterpart to §7, and the section that makes PAS feel like an assistant rather than a
list. Here PAS proactively *offers to take work* — the follow-up draft, the callback reminder
that becomes a prepared call, the lead that needs a check-in, the routine outreach, the
re-engagement message. Work that is real but doesn't require the agent's irreplaceable judgment.

**What delegation feels like:** like handing something to a competent colleague and trusting it
gets done. The agent sees "I can draft the follow-up to the Johnsons, send Maria the listing she
asked about, and queue the three reactivation messages — want me to?" — and with one approval,
it's handled. The feeling is *relief plus leverage*: the agent's reach extends without their
effort.

**How approval works:** PAS proposes, the human disposes (PAS300 §3, §5 — approval-gated
doctrine). Nothing that touches the real world happens silently. Early on, approval is explicit
and per-action — the agent reviews and confirms. As trust builds and the agent configures it
(PAS304), more becomes pre-authorized within bounds the agent set. The progression is from "ask
me every time" to "handle these kinds of things and tell me what you did" — but the agent always
owns the dial, and PAS never crosses it. Delegation that betrays trust once is delegation the
agent never uses again, so the bar is: PAS would rather ask than overstep.

---

## 9. "What I forgot"

One of the strongest adoption surfaces in the entire product, because it targets the agent's
deepest professional fear: the dropped ball that costs a deal or a relationship.

**Why it creates habit:** every agent carries a low-grade, constant anxiety — *what am I
forgetting?* It's the tax of the job. The first time PAS says "you told the Patels you'd call
them back Tuesday and it's Thursday," and the agent realizes PAS caught something they'd lost,
the relationship changes permanently. PAS becomes the thing that *has your back*. That single
moment of "PAS saved me" is worth more than any feature, and it compounds: once an agent has
felt it, *not* opening PAS feels reckless. The habit forms not because PAS is sticky, but because
the agent can no longer afford to fly blind.

**What belongs here:** the dropped promise (a callback committed and not made), the cold lead
(someone who went quiet and was never re-engaged), the stalled deal nobody pushed, the follow-up
that aged past its window, the client who hasn't been touched in too long. Specifically, the
commitments and threads that *the agent themselves* let slip — surfaced kindly, framed as "here's
what I caught for you," never as "here's where you failed." The tone is a teammate covering for
you, not a manager logging your misses. The difference in framing is the difference between
adoption and resentment.

---

## 10. Opportunity discovery

The cockpit must surface **upside, not just risk.** A product that only ever shows problems
becomes a source of stress; the agent starts to dread opening it. PAS balances every "here's
what's slipping" with "here's what's worth doing" — because the agent's job is not just to avoid
dropping balls, it's to make money, and PAS should actively help them find it.

PAS surfaces the opportunities buried in the agent's own data that they'd never dig out
themselves:

- **Neglected leads** — someone who showed real interest months ago and was forgotten; warm, not
  cold, if touched now.
- **Reactivation opportunities** — past clients at a natural re-engagement moment (an
  anniversary, a market shift, a life event PAS knows about).
- **Referral opportunities** — happy clients who are statistically ripe to refer, and the
  natural moment to ask.
- **Pipeline opportunities** — the deal one nudge away from moving, the stage where a small
  action has outsized leverage.

The philosophy: the agent's CRM is full of money they've forgotten about. PAS's job is to find
it and hand it to them at the right moment — not as a report ("you have 40 dormant leads") but
as an action ("the Riveras bought through you 3 years ago and the market in their area just
shifted — good time to reach out, want a draft?"). Opportunity discovery is how the cockpit makes
the agent *more*, not just *safer*.

---

## 11. Follow-up protection

Follow-up is core ORVN doctrine — the callback wedge (PAS300 §18) made personal. In real estate,
the deal is usually lost not to a competitor but to silence: the follow-up that never happened.
PAS treats **a commitment as sacred.**

**How PAS thinks about commitments:** every promise the agent makes — "I'll call you back
Tuesday," "I'll send that over this afternoon," "let's reconnect next month" — is a debt PAS
tracks and protects. PAS knows what was promised, to whom, by when, and it will not let it
silently lapse. Commitments are surfaced *before* they're due (so they're kept, not just
mourned), with time pressure made honest and obvious. A commitment going cold is the single most
preventable loss in the agent's business, and preventing it is the cockpit's most concrete daily
value.

**What agents experience:** the quiet confidence that nothing they promised will fall through —
that PAS is holding the thread even when they forget it. The agent stops carrying the mental load
of "did I follow up?" because PAS carries it for them. Over time this becomes the trait agents
describe to other agents: *"PAS makes sure I never drop a client."* That sentence is the
distribution engine (PAS302 §17). Follow-up protection isn't a feature of the cockpit; it's the
promise the cockpit keeps.

---

## 12. Coaching layer

Personal coaching — and the word *personal* is load-bearing. This is **not** brokerage coaching,
not manager coaching, not a performance review. It is private, on the agent's side, and it never
travels upward (PAS301 §22; PAS302 §15 cardinal failure).

**What PAS coaches:** the craft. How a call went and what might have landed better. A script
that keeps losing people at the same point. A pattern in won vs. lost deals the agent can't see
from inside. The habit that, changed slightly, would compound. Coaching is specific, kind, and
**evidence-backed** — drawn from real calls and real outcomes, not generic advice — and it's
always *one doable thing*, not a report card of weaknesses.

**What must never be visible upward:** all of it. An agent's coaching content — their weak spots,
their missed opportunities, their improvement areas — is theirs alone. No broker, no team lead,
no manager ever sees it. The moment coaching could be read by someone who evaluates the agent, it
stops being coaching and becomes surveillance, and the agent stops being honest with PAS (and
PAS stops being useful). The wall here is absolute and structural (PAS301 §§4, 22), not a
setting.

**What belongs only to the agent:** their coaching history, their personal performance trends,
their candid weak spots, the record of how they're getting better. This is class-A person-owned
capital (PAS301 §4) — it follows them everywhere and is seen by no one else. The agent must be
able to feel, in their bones, that telling PAS the truth about a bad call has no cost. That
safety is what makes the coaching work.

---

## 13. Personal growth layer

Coaching addresses today's call; the growth layer addresses the agent's trajectory. PAS helps
the agent get *better over time* — at skills, habits, communication, scripts, confidence, and
performance — and makes that improvement *visible to the agent* as a source of pride and momentum.

The agent should be able to feel themselves getting sharper: scripts that are improving because
PAS helped refine them, habits that are sticking, a closing rate that's trending up, conversations
that land better than they did three months ago. PAS reflects this back not as a leaderboard
position but as a personal arc — *you are becoming a better agent, and here's the evidence.*

The discipline: **this must never become a gamified productivity app.** No points-for-points,
no streaks-as-the-point, no manufactured competition, no dopamine slot machine. Streaks and
progress exist only as honest reinforcement of the agent's *own* commitments and growth
(PAS300 §17 — "addictive through utility, not gamification alone"). The line is simple: if a
growth feature would still matter to the agent with the numbers hidden, it's real; if it only
works because of the numbers, it's manipulation. PAS stays on the real side of that line. Growth
is felt as mastery, not as a game.

---

## 14. PAS relationship model

The most important conceptual section in this document, because it determines everything else.
*What is PAS, to the agent?* Hold the candidates up:

- **CRM** — wrong. A CRM is a database the agent serves; PAS serves the agent.
- **Assistant** — close, but too junior. An assistant does what it's told; PAS has a point of
  view and acts ahead of instruction.
- **Coach** — part of it (§12), but a coach only advises; PAS also *does the work.*
- **Accountability partner** — part of it (§§9, 11), but too narrow; that's one thing PAS does,
  not what it is.
- **Operating system** — too cold and infrastructural; an OS has no point of view and no side.
- **Chief of staff** — the closest model.

> **PAS is the agent's chief of staff.**

A chief of staff is the right model because it is the only one that holds all of it at once: it
**knows everything** about the principal's world, **decides what matters** and protects their
attention (§§5–7), **takes work off their plate** and reports back (§8), **catches what they
forgot** (§9), **finds them opportunities** (§10), **coaches them privately and loyally**
(§12), and is **unmistakably on their side** — it works *for the agent*, not for the
organization above them. A chief of staff has judgment, takes initiative, and earns trust by
being right and discreet. That is exactly the relationship PAS300's "Proactive Assistant" points
at, made concrete: proactive (acts ahead of you), assistant (serves you), at scale (one chief of
staff per agent, for every agent). Every design decision in the cockpit can be checked against
one question: *is this what a brilliant, loyal chief of staff would do?* If yes, build it. If
no — if it's something a database, a manager, or a game would do — don't.

---

## 15. PAS Chat inside the cockpit

Chat lives inside the cockpit as the way the agent *talks to their chief of staff* — not as a
chatbot in a corner. Its role is to let messy human intent meet a system that already has the
agent's whole world loaded: "who should I call first?", "draft a follow-up to the Hendersons,"
"what did I promise the Patels?", "remind me about this lead next week." Chat is the conversational
surface of the same companion the brief speaks with — same voice, same context, same point of
view (PAS305).

**What chat does:** turns intent into grounded, approval-gated action; retrieves the agent's own
context to answer; proposes the next move. It is the cockpit becoming responsive — the agent can
*ask*, not just receive.

**What chat must never be:** a generic chatbot the agent has to coax, a trivia toy, or a blank
box that forgets who the agent is between messages. It is not a place the agent goes to "use the
AI" — it's the natural way they direct their chief of staff. The chatbot framing is poison: it
makes PAS feel like a novelty instead of an operator. Chat in the cockpit always knows the
agent's book, always cites its evidence, and always proposes rather than just chats.

---

## 16. PAS Brain inside the cockpit

The Brain is how the cockpit *knows* — but the agent should rarely experience it as a separate
"knowledge base." It should feel like the chief of staff simply *remembering.*

**Personal memory** appears as PAS recalling what it knows about the agent's clients, deals, and
preferences — surfaced in context ("you noted the Hendersons want a yard for the dog") rather
than filed in a vault the agent has to visit. Memory is inspectable and correctable (PAS300 §10):
the agent can see what PAS remembers and fix it, because trust requires the agent know what's in
the chief of staff's head.

**Knowledge** — the agent's own scripts, references, market notes — appears when relevant, cited
to its source (evidence-backed doctrine, PAS300 §3), so the agent can trust an answer and see
where it came from.

**Uploads** — the agent dropping in a contract, a listing, a set of notes — feel like handing a
document to the chief of staff and saying "know this." PAS ingests it, proposes what it learned
(memory candidates, approval-gated; PAS301 §19), and the agent confirms what becomes trusted.
The experience is *teaching your assistant*, not *administering a database*.

**How the agent experiences memory:** as a companion that remembers their world so they don't
have to — quietly, accurately, and only ever within their own workspace (PAS301 §20 isolation).
The Brain is most successful when the agent never thinks about it as a feature at all, only as
*PAS knows me.*

---

## 17. Workspace context

The cockpit is the agent's home, and home travels with them (PAS301 §16). What stays constant
across every workspace the agent belongs to: the cockpit *is theirs* — their chief of staff,
their voice for PAS, their coaching, their personal capital — and it is always one switch away
(PAS301 §7). The relationship doesn't change shape because the agent joined a brokerage.

What changes by workspace:

- **Personal workspace:** the full personal cockpit — self-sourced leads, private notes, private
  coaching. Everything is the agent's and seen by no one.
- **Team workspace:** the cockpit additionally reflects the agent's *team* obligations — shared
  callbacks, team commitments they own, team scripts — while the agent's personal coaching and
  private workspace stay invisible to the team (PAS301 §22). The agent sees "what I owe the team"
  without the team seeing "how the agent is doing privately."
- **Brokerage workspace:** the cockpit reflects brokerage standards and brokerage-sourced work
  the agent is responsible for, within the brokerage's configured frame (PAS304), while —
  again — the personal layer remains private.

The constant is the most important thing: **no matter whose workspace the agent is working in,
the cockpit never becomes a window the broker looks through.** The agent's experience of "PAS is
mine and on my side" is identical in their personal workspace and inside a brokerage. The "one
you, many doors" model (PAS301 §24) means the agent walks through different doors but is always
themselves, with their own chief of staff, on the other side.

---

## 18. Notifications

Notifications feed the cockpit, but the cockpit is not a notification dump. The philosophy: a
notification exists only to **protect a commitment or surface a consequential opportunity** that
the agent can act on now (PAS302 §10) — never to manufacture engagement.

**Priority:** there are effectively two tiers. *Now* — a commitment about to lapse, a hot lead
cooling fast, a time-sensitive opportunity — which is worth interrupting the agent for. And
*later* — everything else, which is folded into the next brief rather than pushed. PAS defaults
to *later* and earns the right to interrupt only when the cost of waiting is real.

**Avoiding overload:** the cockpit's whole posture is anti-noise (PAS300 §17 — calm). If PAS
ever trains the agent to swipe notifications away without reading them, it has lost — because the
one that mattered gets swiped too. Every notification is therefore rare, specific, and
actionable. The cockpit batches the rest into the brief, where they belong. Calm is not a
feature here; it's a survival requirement for trust.

---

## 19. Addiction loop

The term, used carefully and honestly: the goal is **habit through usefulness, never habit
through manipulation** (PAS300 §17; PAS302 §14). PAS does not use dark patterns, manufactured
urgency, variable-reward slot mechanics, or guilt. The loop is built entirely on being genuinely
the best first move of the agent's day.

The loop works like this. Each morning the agent opens PAS and gets a real payoff — relief and a
plan (§4). They act on it, and PAS makes them money or saves them from a dropped ball (§§9–11).
That outcome teaches the agent that opening PAS *first* is the rational move. The more they use
it, the more PAS knows, the better its briefs and catches get (§16) — so the value compounds and
leaving would mean losing accumulated leverage. The end-of-day review closes the loop with a
sense of completion, and the next morning's brief opens it again. Rhythm, not slot machine.

Why PAS becomes the first tab opened every morning: because it is the fastest, calmest path from
"I just woke up" to "I know exactly what to do and nothing is slipping." No other tool gives the
agent that, and once they've felt it, starting the day any other way feels like flying blind.
The addiction is to *being in control of the day* — and PAS is just the most reliable way to feel
it. That is a habit worth having, which is the only kind PAS will build.

---

## 20. Failure modes

The cockpit can fail in specific, predictable ways. Each must be designed against:

- **Feels like a CRM.** If the agent has to *feed* the cockpit — enter data, update records,
  maintain it — it's dead. The cockpit must give more than it asks. The moment maintenance
  exceeds value, the agent abandons it. PAS must read the agent's world, not demand the agent
  populate it.
- **Feels like surveillance.** The cardinal failure (PAS302 §15). If anything in the cockpit
  feels like it's reporting upward — if coaching could be seen by a manager, if the agent senses
  they're being graded — trust dies instantly and permanently. Private must *feel* private, not
  just be private.
- **Too much information.** A cockpit that shows everything is a dashboard wearing a costume. If
  the agent has to triage the cockpit itself, it has failed at its one job (§2). The discipline
  of *less* is the product.
- **Too many widgets.** Every panel added dilutes the point of view. A cockpit assembled from
  modules is a wall-of-modules (PAS300 §5) — the thing PAS is explicitly escaping. The cockpit is
  an edited briefing, not a configurable grid.
- **Not enough action.** If the agent can only *read* the cockpit and must go elsewhere to *do*,
  it's a report. Every important thing surfaced must be actionable in place (PAS300 §5
  describe→act). A cockpit you can't act from is just a prettier dashboard.
- **Wrong point of view.** If the brief's priorities are consistently off — surfacing trivia,
  missing the deal that mattered — the agent stops trusting it, and a briefing you don't trust is
  worse than no briefing. Being *right* is the cockpit's credibility, and credibility is the whole
  asset.
- **Slow.** Latency kills the morning habit (PAS300 §17). A chief of staff who makes you wait
  isn't worth opening first.
- **Generic.** A brief that could belong to any agent belongs to none. The personalization is the
  product (§6); without it, the cockpit is a newsletter.

The throughline of every failure mode: the cockpit fails the moment it asks more of the agent
than it gives, or the moment it stops feeling like it's on the agent's side.

---

## 21. Things the cockpit must never become

Explicit anti-goals:

- **A data-entry chore** — it reads the world; it does not make the agent maintain it.
- **A surveillance instrument** — nothing in it ever serves a manager at the agent's expense.
- **A dashboard** — it decides and acts; it does not merely display.
- **A configurable widget grid** — it has a point of view; it is not a blank canvas the agent
  must assemble.
- **A notification firehose** — it is calm by design; it earns every interruption.
- **A gamified productivity app** — growth is mastery, not points (§13).
- **A generic chatbot** — chat is directing a chief of staff, not coaxing an AI (§15).
- **A CRM clone or a Slack clone** (PAS300 §21) — it is neither a filing cabinet nor a channel
  firehose.
- **A feature museum** — every surface must earn its place by making the core job (§2) better;
  anything that doesn't is removed.

---

## 22. Future expansion

The cockpit is the hub future surfaces plug into — each must *strengthen the core job* (§2) or it
doesn't belong. Compatibility-only notes (these are not designed here):

- **Skills** (PAS307) — new capabilities the chief of staff can wield, appearing as new things
  PAS "can handle" (§8), not as a separate app.
- **Marketplace** — enabling new skills/capabilities; surfaced in-context when they'd help, never
  as a store the agent must browse.
- **Referrals** — an extension of opportunity discovery (§10), surfaced at the natural moment.
- **Recruiting** — relevant to agents who grow into team leads/owners; plugs in via role
  (PAS302 §16) without changing the agent cockpit.
- **Transaction support** — closing logistics surfaced as protected commitments and handle-able
  work, not a separate transaction module.
- **Coaching programs** — structured growth layered onto the personal coaching arc (§§12–13),
  always private to the agent.
- **Document intelligence** — deeper Brain ingestion (§16), appearing as PAS "knowing more,"
  not as a document-management product.

The rule for all of them: they enter the cockpit as *things the chief of staff can now do for
you*, never as new tabs the agent has to learn. The cockpit's coherence is protected above any
individual surface.

---

## 23. Product standard

The quality bar, stated as an outcome. If an agent opens PAS every morning for 90 consecutive
days, PAS must have successfully become **the agent's chief of staff — the trusted first move of
every working day, the thing without which the agent now feels exposed.**

Concretely, by day 90:
- The agent reaches for PAS *before* Gmail, CRM, and texts, instinctively (§3).
- PAS has caught things the agent would have dropped, and the agent *knows* it has — there is at
  least one "PAS saved me" memory, probably several (§9).
- PAS has handed the agent opportunities they'd have missed, and some became money (§10).
- The agent trusts the brief's judgment enough to act on it without re-checking everything (§6).
- The agent has told another agent about it (the distribution proof, PAS302 §17).
- Removing PAS would feel like losing a colleague, not uninstalling an app.

If those are true at 90 days, agent adoption is real and the distribution thesis is alive. If
they're not, the cockpit has failed its one job, and no amount of features downstream will save
it. This is the bar every future PAS decision is measured against (PAS300 §22 made personal).

---

## 24. Final standard

> **The Agent Cockpit exists so an agent never has to wonder what matters, what is slipping, what
> is worth doing, or what PAS can do for them next.**

---

### Validation note

This document is **docs-only**. It makes **no** changes to UI, frontend, backend, auth, CORS,
packages, the PAS209 work, or the parked stash. It defines the Agent Cockpit's product
philosophy and the surfaces, relationship model, and quality bar that PAS304 (Configuration) and
PAS305 (Chat) build toward; it implements none of it. Nothing is pushed.
