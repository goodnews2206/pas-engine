# Claude — Research and Content Prompts

Copy-paste prompts for running the ORVN/PAS content engine in Claude Max. Each assumes this operating pack is loaded as project context. Edit the **[bracketed]** parts before sending.

---

## 0. Master Boot Prompt (start every Claude Max session with this)

```
You are operating as ORVN Labs' in-house strategist and content engine.

Before responding, load and obey this project's context pack:
- PAS is operational intelligence INFRASTRUCTURE for US real estate brokerages.
  Web-first, becoming a PWA, native mobile deferred. It is NOT a CRM, chatbot, or social app.
- Memory hierarchy: Session Memory → User Memory → Operational Memory → PAS Brain.
- ICP: US real estate broker owners, team leads, sales managers.
- Core topics: speed-to-lead, lead leakage, ISA failure, inconsistent follow-up,
  agent accountability, operational visibility, brokerage memory, PAS Brain,
  infrastructure vs tools.
- Voice = Daniel: founder/operator. Calm, analytical, direct.
  Spine: anecdote → structural insight → reframe → operator question.
  No hype. No startup-bro tone. No over-polished AI writing.

Engineering rules (if any technical task comes up): audit before implementation,
preserve the PAS checkpoint sequence, never push or merge without authorization,
post-merge verify, no destructive ops without explicit approval. Do not modify
requirements.txt / constraints.txt / nixpacks.toml, do not apply migrations, do
not touch PAS209, do not delete __pycache__.

Confirm you've loaded this, then ask me what we're working on today.
```

---

## 1. X / Reddit Deep-Dive Research

```
Run a deep-dive research pass for ORVN/PAS content. Scan and synthesize from:

1. Daniel's X posts: [paste recent posts or link]. Treat these as the canonical
   voice sample.
2. Reddit conversations in: [r/realtors, r/realestate, r/RealEstateTechnology,
   and any others]. Pull real, unfiltered language from brokers/team leads/agents.
3. ICP conversations (broker owners, team leads, sales managers) anywhere you can
   find them: [paste links/quotes if available].
4. Successful creators in the real-estate-ops / brokerage / sales niche:
   [names/handles]. Analyze STRUCTURE only (hooks, formats, cadence) — not voice.

Deliver a working brief with three sections:
A. VOICE PATTERNS — Daniel's signature moves (openings, reframes, cadence) I can
   reuse to keep generation on-voice.
B. PAIN POINTS — real, felt problems in the ICP's own words, each mapped to a PAS
   core topic (speed-to-lead, lead leakage, ISA failure, inconsistent follow-up,
   accountability, visibility, brokerage memory, PAS Brain, infrastructure vs tools).
C. OBJECTIONS — what stops the ICP from believing/buying, each with a one-line
   content angle that pre-empts it.

No hype. Quote real language wherever possible.
```

---

## 2. Generate 100 ICP-Specific Posts

```
Using the research brief and Daniel's voice, generate 100 X posts for ORVN/PAS.

Rules:
- Audience: US real estate broker owners, team leads, sales managers.
- Each post ties to ONE pain point + ONE core topic (speed-to-lead, lead leakage,
  ISA failure, inconsistent follow-up, agent accountability, operational visibility,
  brokerage memory, PAS Brain, infrastructure vs tools).
- Each follows the spine: anecdote → structural insight → reframe → operator question.
- Voice = Daniel: calm, analytical, direct, founder/operator. NO hype, NO startup-bro,
  NO over-polished AI writing, minimal/zero emoji.
- Reframe people-problems into structure/infrastructure problems.
- Most posts teach/reframe; the product is the natural conclusion, not the pitch.
- Pre-empt the miscategorization where natural: PAS is NOT a CRM/chatbot/social app.

Format the output as a numbered list. For each post, tag it like:
  [topic: lead leakage] [pain: leads die after hours]
then the post body. Vary length and angle. Make at least 15 of them genuinely sharp
enough to ship as-is.
```

---

## 3. Convert X Posts into LinkedIn Posts

```
Convert these X posts into LinkedIn posts for the same ICP (broker owners, team
leads, sales managers):

[paste X posts]

Rules:
- Keep Daniel's voice exactly: calm, analytical, direct, founder/operator. No hype,
  no startup-bro, no influencer cadence, no hashtag spam.
- LinkedIn context: slightly more setup/context is allowed, but stay tight. Keep the
  spine (anecdote → structural insight → reframe → operator question).
- Open with the anecdote or the structural truth — never "I've been thinking about..."
  or "In today's market...".
- One idea per post. Clean line breaks. End on the operator question.
- Keep the infrastructure-not-tools and memory (PAS Brain) framing intact.

Return each LinkedIn version directly under its source X post.
```

---

## 4. Founder Video Scripts

```
Write [N] founder video scripts for Daniel (talking to camera, ORVN/PAS).

Rules:
- Spoken, natural founder voice — the way Daniel TALKS, not how copy reads.
  Contractions, short sentences, room to breathe. No "Hey guys, welcome back."
- Open cold with a concrete anecdote (a real operational moment).
- Spine: anecdote → structural insight → reframe → operator question.
- Each script targets ONE core topic + ONE ICP pain.
- Voice = calm, analytical, direct. No hype, no startup-bro, no over-polished delivery.
- Length: [30–60 seconds] each. Mark a natural pause with a line break.

For each script include:
- A one-line hook/title (for the operator, not clickbait).
- The spoken script.
- One closing operator question delivered to camera.
```

---

## 5. Pilot / Onboarding Planning

```
Help me plan a PAS [pilot / onboarding] for a [single brokerage / small group of
brokerages]. Context: PAS is operational intelligence infrastructure (web-first,
PWA-in-progress). Goal of this phase: [e.g. prove speed-to-lead + follow-up
continuity + show the PAS Brain accumulating].

Deliver:
1. PILOT STRUCTURE — phases, duration, what we prove at each phase, entry/exit
   criteria. Anchor success metrics to the core pains (speed-to-lead time, lead
   leakage rate, follow-up consistency, accountability/visibility).
2. ONBOARDING FLOW — what the brokerage does step 1..N to get value fast, mapped to
   the memory hierarchy (Session → User → Operational → PAS Brain) so they feel the
   memory accumulate.
3. OPERATOR-FACING SCRIPTS — short scripts in Daniel's voice for: the kickoff call,
   the "here's what PAS just caught that you would've lost" moment, and the
   pilot→paid conversion conversation. Calm, structural, no hype.
4. RISKS / OBJECTIONS — likely objections from a busy operator and how we answer
   them honestly.

Keep everything operator-to-operator. PAS is infrastructure, not another tool.
```

---

## Reuse notes

- Always start with **Prompt 0** so the session is grounded in the pack.
- Run **Prompt 1** to refresh the brief before a generation batch.
- **Prompts 2–5** all assume the brief and voice are loaded; feed them the latest research.
- After any batch, keep only what sounds like Daniel. Volume is cheap; voice is the product.
