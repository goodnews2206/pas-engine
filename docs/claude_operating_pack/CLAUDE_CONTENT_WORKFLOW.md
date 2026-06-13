# Claude — Content Workflow

This is the repeatable pipeline for producing ORVN/PAS content with Claude. It moves from **research → extraction → generation → repurposing**. Run it in order. The actual copy-paste prompts live in `CLAUDE_RESEARCH_AND_CONTENT_PROMPTS.md`.

## The pipeline

```
1. RESEARCH            2. EXTRACT             3. GENERATE            4. REPURPOSE
   scan sources    →     voice + pain    →     ICP posts        →     LinkedIn
   (X, Reddit,           + objections          in Daniel's            video scripts
    ICP, creators)                             voice                  pilot/onboarding/ad
```

## Stage 1 — Research / scan

Scan four source types. Capture raw material; don't editorialize yet.

1. **Daniel's X posts** — the canonical voice sample. This is the ground truth for tone. Pull recurring phrases, structures, and the topics that land.
2. **Reddit conversations** — where brokers, team leads, and agents talk unfiltered (e.g. real-estate / brokerage / sales subreddits). Mine real language and real pain.
3. **ICP conversations** — broker owners, team leads, sales managers talking anywhere (X threads, comments, forums, reviews). What they complain about, in their words.
4. **Successful creators in the niche** — what's working structurally (hooks, formats, cadence) — *without* copying their voice. Steal structure, never tone.

## Stage 2 — Extract

From the research, pull three things into a working brief:

1. **Voice patterns** — Daniel's signature moves (anecdote-first openings, structural reframes, operator questions, plain calm cadence). This keeps generation on-voice.
2. **Pain points** — the real, felt problems mapped to PAS core topics (speed-to-lead, lead leakage, ISA failure, inconsistent follow-up, accountability, visibility, brokerage memory, PAS Brain, infrastructure-vs-tools).
3. **Objections** — what stops the ICP from buying or believing ("we already have a CRM," "AI is a gimmick," "my team just needs to try harder," "another tool we won't use"). These become content angles and pre-empts.

## Stage 3 — Generate

Produce **ICP-specific posts in Daniel's voice**:

- Each post tied to a pain point + a core topic.
- Each follows the spine: anecdote → structural insight → reframe → operator question.
- Each obeys `DANIEL_VOICE_AND_TONE.md` (no hype, no startup-bro, no over-polished AI).
- Use the "100 ICP posts" prompt for volume; cherry-pick and refine the best.

## Stage 4 — Repurpose

One idea, many surfaces:

- **X → LinkedIn.** Adapt X posts to LinkedIn's operator/professional context — slightly more context, same voice, no hashtag spam, no influencer cadence.
- **Video scripts.** Convert the strongest ideas into natural spoken founder scripts (talking to camera, not reading copy).
- **Pilot / onboarding / ad scripts.** Conversion-context content — still Daniel's voice, now pointed at a specific action (start a pilot, complete onboarding, respond to an ad).

## Operating principles for every stage

- **Voice is sacred.** When in doubt, re-read `DANIEL_VOICE_AND_TONE.md` and rewrite.
- **Pain before product.** Lead with the operator's reality; PAS is the conclusion, not the opener.
- **Infrastructure framing.** Always pull toward "the layer you run on" and "your brokerage's memory."
- **Pre-empt the miscategorization.** Not a CRM, not a chatbot, not a social app.
- **Volume then taste.** Generate widely, then ruthlessly keep only what sounds like Daniel.

## Suggested cadence

1. Run a **research deep-dive** (Stage 1–2) periodically to refresh the pain/objection/voice brief.
2. Run **generation** (Stage 3) against the fresh brief to produce a batch.
3. **Repurpose** (Stage 4) the winners across LinkedIn + video + conversion scripts.
4. Feed performance back into the next research pass.
