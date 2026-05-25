# PAS UI/UX Reference Study

> Status: draft v1. Owner: ORVN Labs. Last updated: 2026-05-25.
> Reconciliation study between the `ui-ux-pro-max` design intelligence
> system and the PAS product doctrine (Product Design Book + four
> architecture docs). This is the design-language reconciliation
> phase. **No frontend implementation; no component code.**

## 0. What this study is, and how it was done

`ui-ux-pro-max` is a Claude Code Skill that generates design systems
from a reasoning engine over CSV catalogs: 161 product-type
categories, 67 UI styles, 161 color palettes, 24 landing-page
patterns, and 57 typography pairings. Its delivery is **a design
system per project**, not a UI library to copy. Its philosophy is
explicit and worth quoting:

> "Avoid (Anti-patterns): Bright neon colors + Harsh animations +
> Dark mode + AI purple/pink gradients."
> *(from the system's banking/fintech mood output)*

> "No emojis as icons (use SVG: Heroicons/Lucide); cursor-pointer on
> all clickable elements; prefers-reduced-motion respected."
> *(pre-delivery checklist)*

Sources studied:
- Canonical upstream: `nextlevelbuilder/ui-ux-pro-max-skill` (82.5k
  stars).
- Daniel's fork: `goodnews2206/ui-ux-pro-max-skill` — confirmed at
  parity with upstream (0 ahead / 0 behind / 0 fork-only files) on
  2026-05-25. See §17 for the fork-reconciliation pass that retired
  this caveat.

**This is not a copy of `ui-ux-pro-max`.** It is a reconciliation: we
keep its strongest disciplines, discard the parts that conflict with
PAS's product doctrine, and translate the rest into PAS-specific
choices.

---

## 1. What `ui-ux-pro-max` does well

| Strength | Why it matters |
|---|---|
| **Explicit anti-patterns.** Every generated system lists what to *avoid*, not just what to do. | Mirrors PAS's invariant-first posture (live_behavior_changed=False, no hidden automation). Discipline as a *first-class output*. |
| **Pre-delivery validation checklist.** No emojis as icons; cursor-pointer on clickables; prefers-reduced-motion respected; WCAG AA contrast 4.5:1; focus states visible for keyboard nav. | Forces accessibility and craft *before* a surface ships. Adopt directly. |
| **Mood-anchored systems.** Each palette/typography choice ties to a mood (luxury / fintech / AI-native / accessible). Decisions don't float; they answer "for what feeling, for what audience". | PAS has a single, clear mood — *calm operating partner* — and every token should anchor to it. |
| **Decision conditions and matching rules.** Reasoning engine selects style+palette+typography by industry and mood, not by trend. | PAS will similarly drive component selection by *role + module + state*, not by visual fashion. |
| **Concrete numeric guidance.** Transitions 150–300 ms; breakpoints 375 / 768 / 1024 / 1440 px; contrast 4.5:1. | Numbers eliminate debate. Adopt the same number-first discipline. |
| **WCAG AA as floor.** Not a feature — a baseline. | Same posture for PAS. |
| **Multi-platform reasoning.** Same system maps to React, Next.js, SwiftUI, Flutter, Jetpack Compose. | PAS is web-first in v1, but the design tokens should be portable enough to survive a future mobile/native client without rework. |
| **Anti-AI-aesthetic stance.** Calls out "AI purple/pink gradients" as anti-pattern for serious products. | Confirms PAS's instinct: *don't dress up as an AI*. Look like operations software. |

---

## 2. What PAS should adopt

The following move into the PAS design system without modification:

1. **Anti-pattern discipline** — every design decision has a *don't*
   list alongside the *do* list.
2. **Pre-delivery checklist** — accessibility + craft floor must
   pass before any surface ships.
3. **150–300 ms transition window** — PAS interactions land here.
4. **Breakpoints 375 / 768 / 1024 / 1440** — the dashboard adopts these
   exact values.
5. **WCAG AA contrast (4.5:1) as floor.** Visible focus states.
   `prefers-reduced-motion` respected. SVG icons (Heroicons / Lucide),
   never emoji.
6. **Mood-first decisions.** Every visual token explains *which PAS
   mood it serves* — calm, signal, action, danger, demo.
7. **8-point spacing baseline.** A standard borrowed from premium
   product design and consistent with `ui-ux-pro-max`'s density
   guidance.
8. **Cursor affordance on every clickable.** No "wait, is this
   clickable?" moments.

---

## 3. What PAS should NOT adopt

Equally important. The following appear in `ui-ux-pro-max` as
*available styles*, but they conflict with PAS doctrine and are
**rejected**:

| Rejected | Why |
|---|---|
| **Bright neon, vaporwave, cyberpunk, brutalism, Memphis, Y2K, Gen Z chaos** — any "trend" mood. | PAS is operations software for a brokerage owner running a business. Trend aesthetics age fast and read as performative. |
| **AI purple/pink gradients.** | The skill itself flags this as anti-pattern for serious products. PAS does not dress up as an AI. It looks like a senior staff member, not a robot. |
| **Bento-box marketing-grid maximalism** as the primary dashboard layout. | Reads as landing page. PAS is daily-use software; clarity beats density. |
| **Dark mode as default.** | Operations work happens in many lighting conditions, often beside other LTRs (CRM, calendar). Light is the daytime default; dark is opt-in. |
| **Neumorphism / glassmorphism / claymorphism** at any scale that obscures contrast or hit targets. | Decorative styles trade legibility for novelty. PAS rejects that trade. |
| **3D / hyperrealism / chromatic aberration / spatial UI** as primary aesthetic. | Out of scope; performance and clarity dominate. |
| **Harsh animations.** Bounce-heavy easing. Long durations (>500 ms) for routine state changes. | Calm partner, not theme park. |
| **"Generated" feel.** Templated hero / "Get started" / SaaS-marketing shapes that suggest the product was assembled from a kit. | PAS feels considered, not assembled. |
| **Emoji as icons** anywhere — including states like "All clear ✅" or "Critical 🚨". | Same anti-pattern called out by the skill. SVG icon set throughout. |
| **Cute illustrations** for empty states. | Empty states are operational facts ("nothing here yet"). They are not opportunities for character art. |

---

## 4. How PAS differs from `ui-ux-pro-max`'s typical output

`ui-ux-pro-max` is a *general-purpose design system generator*. PAS
is *one product with one mood*, used by professional operators every
day. Three differences shape the reconciliation:

### 4.1 PAS is an operating surface, not a one-off dashboard

The closest categories in the upstream's taxonomy are **Executive
Dashboard** + **Real-Time Monitoring** + **Accessible & Ethical**
mood. But PAS is *all three at once*, every day, for the same user.
That means:

- Information density tilts toward "comfortable + signal", not
  "data-dense".
- Real-time elements (PAS thinking, Critical alerts) coexist with
  slow ambient state — both need clear treatment without one
  drowning the other.
- Accessibility is a daily ergonomics concern, not a compliance
  checkbox.

### 4.2 PAS is operator-required by construction

Most premium dashboards optimise for "self-serve". PAS optimises for
"approve before acting". This affects:

- **Authority needs to be visible.** Approve / decline / "ask PAS"
  are first-class UI affordances, not buried buttons.
- **Pending state is everywhere.** Action proposals, recommendations,
  and approvals form a queue that must always be one click away.
- **Demo / rehearsal labels are persistent.** Other products show
  "Test Mode" as an env banner. PAS labels every artifact inline.

### 4.3 PAS speaks

`ui-ux-pro-max` outputs don't anticipate a conversational surface
that pulls modules inline. PAS does. The composer + peek pane + full
thread combination is its own design discipline:

- Composer must be unobtrusive yet always-on (Cmd/Ctrl+K).
- Peek pane must coexist with the active module without stealing
  focus.
- Inline section embeds inside a thread must look like the real
  module, not a stripped preview.

---

## 5. How PAS should feel emotionally

> *Calm. Precise. Operational. Trustworthy. Quietly intelligent.*

PAS is not a chatbot mascot. PAS is the most senior, most level-
headed staff member in the room. Concretely:

- **Calm:** muted base palette, generous whitespace, no decorative
  motion, no sudden visual shifts. Layouts breathe; they do not
  shout.
- **Precise:** every number, every timestamp, every action is
  rendered with concrete values. No "soon" / "a while ago" labels.
- **Operational:** the UI orients to *what to do next*, not to
  marketing storytelling. KPIs live inside modules; the Command
  Center surfaces decisions.
- **Trustworthy:** evidence is one click from any claim. Demo /
  rehearsal labels propagate. No "magic" that the user can't trace.
- **Quietly intelligent:** PAS reasons in the background. It does not
  show off. When it speaks, it has earned the interruption.

When a user closes their laptop at the end of the day, the feeling
should be *"I had help today"*, not *"I'm exhausted from the tool"*.

---

## 6. Interaction philosophy

- **Every interaction has one obvious answer.** Two competing CTAs in
  a card = redesign.
- **Hover states are confirmation, not decoration.** Each tells the
  user "yes, you can act here", not "look how nice I am".
- **Click targets are never below 44×44 dp** on mobile, 32×32 on
  desktop for non-primary controls.
- **Drag is rare and explicit.** Reordering exists where needed
  (Notifications quiet hours, agent routing weights) — always with
  a visible handle and an "or use the buttons" alternative.
- **Keyboard reaches everything.** Cmd/Ctrl+K opens the composer; Esc
  closes drawers; Tab order matches reading order; visible focus
  rings on everything focusable.
- **No surprise navigation.** Clicking a row does not full-page-route
  — it opens an inspector. Full routes are reserved for true context
  changes.

---

## 7. Animation philosophy

- **Durations: 150–300 ms** for routine state changes (matches
  upstream guidance).
- **Easing: 150 ms ease-out** for entrances; **200 ms ease-in** for
  exits. No bounce, no overshoot.
- **Motion conveys causality.** A drawer opens from the side that
  produced it. An approval card collapses into the audit row it
  becomes. Motion explains transitions; it doesn't decorate them.
- **`prefers-reduced-motion: reduce`** kills all non-essential
  motion. Critical-severity attention cues degrade to a colour change
  + position shift, not a flash or pulse.
- **No looping animation** anywhere except the "PAS is thinking"
  presence indicator (subtle, slow, opacity-only).
- **Skeleton loaders > spinners** for known-shape content. Spinners
  are used only for "we don't yet know the shape of the response".

---

## 8. Spacing philosophy

- **8-point baseline.** Tokens at 4 (hairline), 8, 12, 16, 24, 32,
  48, 64, 96.
- **Generous gutters.** Module-level pages have at least 32 px outer
  padding on desktop; 24 px on tablet; 16 px on mobile.
- **One density rhythm per family** (Operate / Notice / People /
  System). System pages can run a step tighter; Operate pages run a
  step looser to support faster reading.
- **Whitespace is content.** Removing space to "fit more" is the
  most common failure mode. Resist.

---

## 9. Color philosophy

A small, deliberate palette. Tokens are *named by role*, never by
hex.

- **Surface** — page, panel, raised, sunken.
- **Ink** — primary, secondary, tertiary, muted.
- **Brand** — restrained; appears in primary CTA + a single accent.
- **Signal** — FYI, Needs Attention, Urgent, Approval Required,
  Critical (mapped in the Design System Definition doc).
- **Action** — primary, secondary, destructive, ghost.
- **Demo** — a dedicated tone used only for rehearsal labels +
  banners. Visually distinct from any severity tone.

Tokens map cleanly to a light and a dark theme. Light is default;
dark is opt-in and ships in v1.x. **No AI gradients.** **No neon.**
Brand colour is a confident, calm hue — not "AI lavender". A specific
palette will be chosen in the Design System Definition doc.

---

## 10. Dashboard density philosophy

- **Default: comfortable.** Suits the largest share of users: a
  broker owner / ops manager scanning the day.
- **Optional: compact.** A per-user toggle in Settings, not per-page
  density.
- **No "ultra-compact".** Density discipline is more valuable than a
  cramming option. If a power user wants more on screen, the answer
  is a better filter, not smaller text.
- **Tables breathe.** Row height 48 px comfortable / 36 px compact.
  Sticky headers. No more than 7 visible columns by default; the rest
  collapse into the inspector.

---

## 11. Mobile philosophy

- **Same modules, smaller surface.** A user does not lose
  capabilities on mobile — they lose only the multi-pane affordance.
- **Approvals on mobile are first-class.** The approval drawer
  re-flows; the approve/decline buttons stay reachable with one
  thumb.
- **PAS composer pinned above the bottom tab bar.** Expanding it
  takes over the screen; collapsing returns to the previous module.
- **No mobile-only features.** Mobile is a viewport, not a different
  product.
- **Critical alerts override quiet hours** on the device's push
  channel; everything else respects them.

---

## 12. Premium-operating-system feel

Five qualities, in order of impact:

1. **Latency.** Sub-100 ms feedback on every interaction. If the
   server is slow, an optimistic skeleton + a calm progress indicator
   keep the surface alive.
2. **Discipline.** Every screen obeys the same grid, the same
   spacing rhythm, the same type scale. Premium reads as *internal
   consistency*, not as expensive ornament.
3. **Restraint.** Fewer colours, fewer weights, fewer shadows than
   you think. "Expensive" software underdraws; it doesn't overdraw.
4. **Honesty.** Demo state, stale data, failures — all named in
   plain language with the next action. Premium products tell the
   truth.
5. **One-click depth.** Every claim has an evidence link in one
   click; every approval is one click + a reason. Depth is reachable
   without ceremony.

---

## 13. What creates trust vs dashboard fatigue

| Builds trust | Builds fatigue |
|---|---|
| Every number has a "why" link. | Numbers float without provenance. |
| The product says "I don't know yet" when it doesn't. | Vague KPIs delivered with confident framing. |
| The same word means the same thing everywhere ("approve" = same flow on every surface). | Synonyms ("authorise", "confirm", "OK"). |
| Calm typography hierarchy — three weights max. | A dozen sizes and weights competing for attention. |
| Module boundaries are stable; the sidebar does not reshuffle. | Personalisation that hides items the user already learned. |
| Loading states reveal what is coming, not just "Loading…". | Indeterminate spinners that block the page. |
| Modals are rare; drawers and inspectors carry depth. | Stacked modals that lose context. |
| Severity colour is consistent and means one thing. | Red used for "delete", "error", "danger", "live", and "important". |
| Demo / rehearsal labels are unmissable. | Test data presented identically to live data. |
| Decisions surface inline; you don't hunt. | Three-click approvals; "open in new tab to act". |

PAS strictly stays in the left column.

---

## 14. What creates operational calm

The hardest quality to design for. It comes from a few specific
choices:

- **A predictable home base.** The Command Center looks the same
  every morning. The user's first 5 seconds always answer: *what
  needs me, what does PAS propose, what's today, what just happened*.
- **Severity that means something.** A Critical badge appears
  only when something is actually critical. Inflation of severity is
  the surest path to fatigue.
- **No flashing, no auto-scroll, no toasts that demand action.**
  Toasts are confirmation, not interruption.
- **PAS speaking with confidence about what it doesn't know.** Honest
  hedging ("evidence is thin — treat as exploratory") is more
  calming than false certainty.
- **Reversibility.** Knowing that most actions can be undone (or are
  scoped to a small bound) reduces hover hesitation.
- **A clear hand-off when PAS can't do something.** "PAS can't act on
  that for you — here's who can." Calm > shame.

---

## 15. Reconciliation table — `ui-ux-pro-max` guidance × PAS doctrine

| `ui-ux-pro-max` capability / mood | PAS decision |
|---|---|
| Bright neon, vaporwave, cyberpunk, brutalism, Memphis, Y2K, Gen Z chaos | **Reject.** Wrong mood for daily ops. |
| AI purple/pink gradient aesthetic | **Reject.** The skill itself flags as anti-pattern. |
| Neumorphism / glassmorphism / claymorphism | **Reject** at any scale that hurts contrast or hit targets. |
| 3D / hyperrealism / spatial UI / chromatic aberration | **Reject.** Out of scope. |
| Bento-box marketing maximalism | **Reject** as primary dashboard pattern. |
| Dark mode as default | **Reject as default.** Light default; dark v1.x. |
| Executive Dashboard mood | **Adopt** as Command Center reference posture. |
| Real-Time Monitoring mood | **Adopt** selectively — for Proactive Observer and Notifications surfaces. |
| Accessible & Ethical mood | **Adopt as foundation.** WCAG AA floor; visible focus; reduced-motion respected. |
| Editorial Grid restraint | **Adopt** for typography and document-style surfaces (Evidence Digest, Audit Logs). |
| Swiss Modernism 2.0 (typographic restraint, generous whitespace) | **Adopt.** Anchor PAS to this. |
| Soft UI Evolution (subtle depth, low-contrast tonal differences) | **Adopt selectively** for surface elevation. |
| 150–300 ms transitions | **Adopt directly.** |
| Breakpoints 375 / 768 / 1024 / 1440 | **Adopt directly.** |
| WCAG AA 4.5:1 contrast | **Adopt as floor, not goal.** |
| SVG icons (Heroicons / Lucide); no emoji | **Adopt directly.** |
| cursor-pointer on clickables | **Adopt directly.** |
| `prefers-reduced-motion` respected | **Adopt directly.** |
| Pre-delivery checklist | **Adopt directly.** Embedded as part of the PAS surface-ready definition (see Design System Definition doc). |
| Anti-pattern lists alongside guidelines | **Adopt directly.** Every design token carries a "don't" alongside the "do". |

---

## 16. Open questions for v2

- Should PAS adopt **one signature interaction** that becomes its
  visual signature (e.g. the way the composer expands, or the way
  evidence digests pull in)? Risk: ornament. Reward: identity.
- Should the Command Center allow a **per-user "first-pin"** — a
  saved view they always land in — or stay uniform by role?
- **Dark mode timing**: ship in v1 or v1.x? Adds tokens, doubles
  visual QA.
- **Brand palette anchor**: a single confident hue (and which) — or
  a near-neutral palette where the only "brand" expression is
  typography and rhythm?
- **Severity colour blindness**: red/amber severity is convention,
  but problematic for ~8% of users. Pair every severity colour with
  a non-colour signal (icon, shape) from day one?
- **Tone of empty-state copy in different modules** — should the
  voice subtly shift (PAS Brain warmer; Audit Logs more clinical)?
  Or hold one voice across the product?
- **Reconciliation with the user's specific fork** — *resolved in §17
  below (2026-05-25).*

---

## 17. Daniel Fork Reconciliation (2026-05-25)

Performed after the user provided the exact fork URL:
`https://github.com/goodnews2206/ui-ux-pro-max-skill`.

### 17.1 What changed after inspecting Daniel's fork

**Nothing in the fork itself.** GitHub's compare endpoint between
`nextlevelbuilder:main` and `goodnews2206:main` reports verbatim:
*"There isn't anything to compare. nextlevelbuilder:main and
goodnews2206:main are identical."*

Concretely:
- 0 commits ahead of upstream.
- 0 commits behind upstream.
- 0 fork-only files, 0 fork-only commits, 0 diff stats.
- Default branch `main` matches upstream `main` byte-for-byte at the
  HEAD of the comparison.

Daniel's fork is a **parity fork** — no brokerage-specific tokens,
no PAS-specific edits, no customised data files, no override
templates. The v1 reference study performed against the canonical
upstream therefore **applies in full** to the fork.

### 17.2 Whether prior conclusions still hold

**Every conclusion from §1–§16 holds.** No reversal, no reordering,
no anti-pattern flipping sides. The reconciliation table in §15 is
unchanged.

The reason for the original §0 caveat (study performed against
upstream rather than the user's fork) is now retired: the two
sources are demonstrably identical at this snapshot. A future drift
in the fork would trigger a new reconciliation pass.

### 17.3 New patterns surfaced by the richer read

Direct verbatim access to the fork's README and `CLAUDE.md` (deeper
than the initial summary read) surfaced a few patterns worth pulling
into PAS doctrine. These are *additive* — they do not contradict any
prior conclusion.

#### 17.3.1 The MASTER + per-page overrides documentation pattern

The skill exposes a documentation strategy worth borrowing for PAS's
own design-system documentation:

```
design-system/
├── MASTER.md            # Global tokens, rules, severity, density, demo
└── pages/
    └── <module>.md      # Module-specific overrides (only deviations)
```

The retrieval rule the skill prescribes is: *check the page file
first; if present, its rules override the master; if absent, the
master is authoritative.*

PAS already has the canonical doctrine in
`docs/pas_design_system_definition.md`. As individual modules ship,
each may carry a thin per-module overrides note under
`docs/design-system/pages/<module>.md` rather than amending the
master file. See the small addition to the Design System Definition
doc (§31) for the formal adoption note.

This is a **documentation** pattern, not a runtime mechanism. PAS
does not need a generator to consume it; humans and downstream agents
do.

#### 17.3.2 Decision-rule discipline alongside tokens

The skill ships 161 industry-specific reasoning rules + 99 UX
guidelines + 25 chart types in CSV-backed databases. The relevant
takeaway for PAS is *not* the catalog itself — PAS is one product —
but the **format**: rules are tabular, named, and carry an explicit
"anti-pattern" column alongside the recommendation.

PAS already adopts this in spirit (anti-pattern lists per design
section). The reconciliation reinforces it as a *required* author
discipline: every design rule we write down carries its negative
twin. This is captured in the existing pre-delivery checklist
(Design System Definition §29) — no new doc change needed.

#### 17.3.3 Single-command access to the design system

The skill provides one CLI command (`uipro init --ai <platform>`) that
materialises the design-system surface in any project. The shape of
that affordance — *one command, one source of truth, regenerable at
will* — is worth keeping in mind for PAS's downstream tooling. We do
not need to ship it in v1, but the future direction (a tiny script
under `scripts/` that emits the current design-token set as CSS
variables or a Tailwind preset) is now signposted.

### 17.4 Anti-patterns PAS should still reject

All anti-patterns from §3 stand verbatim. The richer read added one
useful corroboration: the skill explicitly flags **AI purple/pink
gradients** in the v2 README's banking/fintech example output, and
ships the same anti-pattern across its industry rules. PAS's rejection
of that aesthetic is, by transitive endorsement, consistent with the
upstream's own discipline.

### 17.5 Whether the Frontend Foundation Plan changes

**No change.** The fork has no fork-specific implementation
recommendations, framework preferences, or build-tool choices that
would amend `docs/pas_frontend_foundation_plan.md`. The plan's
framework intent (Next.js), shell structure, state boundaries,
streaming approach, and 15-step implementation sequence are all
unaffected.

### 17.6 Whether the Component Inventory changes

**No change.** The fork does not enumerate components in a form that
adds or removes any item from `docs/pas_component_inventory.md`. The
P0/P1/P2/P3 priority structure stands.

### 17.7 Net effect

| Document | Change required by fork reconciliation |
|---|---|
| `docs/pas_uiux_reference_study.md` | This §17 added; §0 caveat retired; §16 question resolved. No other lines changed. |
| `docs/pas_design_system_definition.md` | One small additive section (§31) documenting the MASTER + overrides documentation pattern as an option for module-specific design notes. |
| `docs/pas_frontend_foundation_plan.md` | No change. |
| `docs/pas_component_inventory.md` | No change. |

The v1 reference study is **confirmed**, not amended.

---

*End of v1 + fork reconciliation 2026-05-25.*
