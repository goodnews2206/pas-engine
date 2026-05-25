# PAS Design Tokens v1 — Locked

> Status: locked. Branch: `pas-web-foundation-v1`. Owner: ORVN Labs.
> Date: 2026-05-25. Implementation: `web/app/globals.css`.
> Authority: `docs/pas_design_system_definition.md`.

This document records every deliberate decision in the locked token
system. It is the source of truth for *why* each token has its value.
Anyone changing a token must update this doc with the new rationale.

---

## Design direction (summary)

| Aspiration | What it means in practice |
|---|---|
| Apple-level simplicity | Fewer tokens, not more. Every token earns its presence. |
| Stripe-level clarity | Numbers are precise; hierarchy is unambiguous. |
| Linear-level restraint | Neutral palette, brand accent used sparingly. |
| Operational calm | No motion that surprises. No colour that shouts. |
| Trustworthy, not flashy | Premium reads as internal consistency, not expensive ornament. |

**Rejected by doctrine** (from `docs/pas_uiux_reference_study.md §3`):
AI purple/pink gradients · neon · glassmorphism · dark-first ·
bento-box maximalism · emoji states · illustration empty states ·
bounce animations · anything "assembled from a kit."

---

## 1. Signature hue

**`#3B52D4` — PAS Deep Indigo**

HSL: approximately 232°, 63%, 52%.

### Why this hue

The previous static dashboard used `#5B3FD4` (hue ~260° — purple-dominant).
The design system doctrine explicitly warns against "AI lavender / purple"
becoming the product identity. The shift is deliberate:

| | Old `#5B3FD4` | New `#3B52D4` |
|---|---|---|
| Hue | ~260° (purple-dominant) | ~232° (blue-dominant) |
| Association | AI product, tech startup | Operational authority |
| Gradient risk | Easily pulled into "AI gradient" aesthetic | Blue-dominant resists that |
| Reference peers | AI chat products | Stripe (~257° but flat+confident), Linear (~235°) |

The new hue reads "calm operational authority" — closer to how a
senior member of staff carries themselves than how an AI chatbot
presents itself.

### Contrast verified

| Background | Contrast | Passes |
|---|---|---|
| `--surface-base` (#F6F6FB) | ~5.8:1 | AA ✓ |
| White (#FFFFFF) | ~6.2:1 | AA ✓ |

### Derived brand scale

| Token | Hex | Use |
|---|---|---|
| `--_br-600` | `#3B52D4` | Primary — signature hue |
| `--_br-500` | `#4D62DC` | Hover state |
| `--_br-700` | `#2B3FB8` | Pressed / active state |
| `--_br-100` | `#EBF0FE` | Ghost tint backgrounds |
| `--brand-subtle` | `rgba(59,82,212,0.08)` | Row hover, selection tint |
| `--brand-muted` | `rgba(59,82,212,0.14)` | Active chip, selection indicator |

### Anti-patterns for brand colour

- Never use as a gradient (`#3B52D4 → anything`).
- Never use for severity signals (signals have their own tokens).
- Never use on more than two elements per screen simultaneously.
- Never use a lighter tint for the primary button (contrast would fail).

---

## 2. Neutral scale

Custom cool-gray with a **subtle blue undertone** (B channel sits
4–8 pts above RG at each step). This is invisible at a casual glance
but subconsciously harmonises the page with the brand indigo. It
prevents the "warm beige drift" of pure warm-gray neutrals.

| Token | Hex | Semantic use |
|---|---|---|
| `--_n-950` | `#0B0B11` | Near-black, rare |
| `--_n-900` | `#111118` | `--ink-primary` |
| `--_n-800` | `#1C1C27` | — |
| `--_n-700` | `#2A2A3A` | `--ink-secondary` |
| `--_n-600` | `#44445C` | `--ink-tertiary` |
| `--_n-500` | `#62627A` | `--ink-muted` |
| `--_n-400` | `#8F8FA8` | `--ink-disabled` |
| `--_n-300` | `#BCBCD0` | `--border-strong` |
| `--_n-200` | `#DCDCE8` | `--border` |
| `--_n-150` | `#E8E8F2` | `--surface-muted` |
| `--_n-100` | `#F0F0F6` | `--surface-subtle` |
| `--_n-50`  | `#F6F6FB` | `--surface-base` (page bg) |
| `--_n-0`   | `#FFFFFF` | `--surface-raised` (cards) |

---

## 3. Semantic colour system

All UI code references semantic aliases, never raw scale tokens.
This is the full set of named semantic roles:

### Surfaces

| Token | Value | Use |
|---|---|---|
| `--surface-base` | `--_n-50` (#F6F6FB) | Page background |
| `--surface-raised` | `--_n-0` (white) | Cards, sidebar |
| `--surface-subtle` | `--_n-100` | Input backgrounds, inset regions |
| `--surface-muted` | `--_n-150` | Chips, hover tints |
| `--surface-sunken` | `#EBEBF3` | Depressed wells, code blocks |

Light-first: all five surfaces are white-to-near-white. No dark
surface values in v1; the stub block in `globals.css` is intentionally
empty until v1.x.

### Ink

| Token | Contrast on surface-base | Use |
|---|---|---|
| `--ink-primary` | ~17:1 | Body copy, headings |
| `--ink-secondary` | ~10:1 | Supporting copy, labels |
| `--ink-tertiary` | ~7:1 | Metadata, eyebrow text |
| `--ink-muted` | ~4.8:1 | Placeholder, helper text |
| `--ink-disabled` | ~3.2:1 | Disabled controls (paired with ARIA-disabled) |
| `--ink-inverse` | white | Text on dark/brand backgrounds |

### Border

| Token | Use |
|---|---|
| `--border` | Default 1px hairline |
| `--border-strong` | Focused inputs, emphasis |
| `--border-brand` | Brand-coloured hairline (active nav, focus ring context) |

### Action

| Token | Use |
|---|---|
| `--action-primary` | Primary button background |
| `--action-primary-hover` | Hover state |
| `--action-primary-dark` | Pressed / active |
| `--action-destructive` | `#B91C1C` — delete / remove only |

---

## 4. Severity colour system

Five severity levels, five distinct hue families. Each **must** pair
colour + SVG icon + positional treatment. Colour alone is never the
only signal (supports 8% of users with colour-vision deficiency).

| Severity | Token | Hex | Approx contrast | Background token | Icon |
|---|---|---|---|---|---|
| FYI | `--signal-fyi` | `#3D5A6C` | ~6.8:1 ✓ | `--signal-fyi-bg` | `info` (Lucide) |
| Needs Attention | `--signal-attention` | `#92400E` | ~6.1:1 ✓ | `--signal-attention-bg` | `bell` |
| Urgent | `--signal-urgent` | `#B45309` | ~4.7:1 ✓ | `--signal-urgent-bg` | `alert-triangle` |
| Approval Required | `--signal-approval` | `#3B52D4` | ~5.8:1 ✓ | `--signal-approval-bg` | `check-circle` |
| Critical | `--signal-critical` | `#991B1B` | ~7.0:1 ✓ | `--signal-critical-bg` | `alert-octagon` |

Note: `--signal-urgent` at ~4.7:1 is close to the floor. Verify with
a contrast checker in component QA; the value passes AA but has no
margin. Never use `--signal-urgent` on text smaller than 14px.

### Severity anti-patterns

- **Never inflate.** If everything is Urgent, nothing is.
- **Never use red for delete/danger controls.** That is `--action-destructive` — a separate token.
- **Never use brand indigo outside `--signal-approval`** for severity.
- **Approval Required uses brand indigo intentionally** — the
  approval action is the primary branded interaction in PAS.

---

## 5. Typography

### Family decisions

| Role | Family | Why |
|---|---|---|
| UI sans | Inter (via `next/font/google`) | Geometric humanist, screen-optimised, variable weight |
| Mono | JetBrains Mono (via `next/font/google`) | Excellent legibility at 11–13px; transcripts, audit logs, numbers |

Both fonts are loaded with `display: swap` and injected as CSS
variables (`--font-inter`, `--font-jetbrains-mono`). Zero CLS risk.

### Type scale (locked)

| Token | Size | Line-height | Letter-spacing | Use |
|---|---|---|---|---|
| `--text-display` | 32px / 40px | — | −0.02em | Page H1, wordmark |
| `--text-title` | 24px / 32px | — | −0.015em | Module headings |
| `--text-subtitle` | 18px / 28px | — | −0.01em | Section headings |
| `--text-body-lg` | 16px / 24px | — | 0 | Default body, table cells |
| `--text-body` | 14px / 20px | — | 0 | Secondary text, labels |
| `--text-caption` | 12px / 16px | — | +0.01em | Timestamps, metadata |
| `--text-micro` | 11px / 16px | — | +0.04em | Chips, badges, tags |

Letter-spacing is negative at large sizes (tightens optical gaps),
slightly positive at small sizes (improves legibility in caps contexts).

### Weight scale

Three weights only: `--fw-regular` (400) · `--fw-medium` (500) · `--fw-semibold` (600).
Weight 700 is reserved for the single signature brand mark (`h1.wordmark`).
No bold in body copy. No thin weights.

### Typography rules (from spec §1.3)

- Numbers in tables: `font-variant-numeric: tabular-nums` — applied globally.
- Timestamps: relative inline ("2h ago"), absolute on hover.
- Sentence case for buttons and labels.
- Title case for module names in sidebar.
- No italic for UI emphasis (italics reserved for transcript proper nouns).

---

## 6. Spacing

8-pt baseline. Ten steps (0 → 96 px). Three module-gutter tokens.
Five semantic flow aliases for consistent rhythm without hardcoded values.

The key principle from `docs/pas_uiux_reference_study.md §8`:
**"Whitespace is content. Removing space to 'fit more' is the most
common failure mode. Resist."**

Desktop outer gutter: `--gutter-desktop` = 32px.
Tablet: 24px. Mobile: 16px.

---

## 7. Radius and elevation

### Radius

Maximum 14px for any rectangular surface (`--radius-lg`). Anything
larger reads as marketing/landing-page, not operations software.
`--radius-pill` (9999px) is for circular elements only: avatars,
status dots, severity chips.

### Shadows

Two shadows, no more.

| Token | Spec | Use |
|---|---|---|
| `--shadow-soft` | 1px compound | Cards, raised panels |
| `--shadow-overlay` | 8px compound | Drawers, peek pane |
| `--shadow-popover` | 4px compound | Menus, tooltips, toasts |

Shadow colour uses `rgba(13, 13, 20, …)` — the darkest neutral with a
blue tinge, matching the neutral scale undertone.

**Elevation invariant:** every elevated surface must carry both
`--shadow-soft` AND a 1px hairline `--border`. Shadow alone is
insufficient for users in high-contrast mode or with low contrast
sensitivity.

---

## 8. Motion timing

| Token | Duration | Easing | Use |
|---|---|---|---|
| `--anim-instant` | 80ms | linear | Hover/press microstate |
| `--anim-fast` | 150ms | `--ease-out` | Entrances |
| `--anim-base` | 200ms | `--ease-in-out` | Drawers, panels |
| `--anim-slow` | 300ms | `--ease-in-out` | Severity surfacing, banners |
| `--anim-presence` | 1200ms | ease-in-out, opacity-only | "PAS is thinking" |

No duration exceeds 300ms except `--anim-presence`. No bounce,
no spring, no overshoot.

`--anim-presence` must stop entirely under `prefers-reduced-motion`
(implemented in the `@media` block in `globals.css`).

**Motion rule:** transitions use `opacity` + `transform` only.
Never animate `width`, `height`, `top`, `left` — these cause layout
thrash and reflow.

---

## 9. Demo / rehearsal label

Token family: `--demo-*`. Warm amber. Structurally distinct from all
severity tokens.

| Token | Hex | Use |
|---|---|---|
| `--demo-bg` | `#FFFBEB` | Chip and banner background |
| `--demo-ink` | `#78350F` | Label text (~9:1 on demo-bg ✓) |
| `--demo-border` | `#B45309` | Visible chip border |

**Immutability rule (§26):** The demo token family is non-overridable
by user theme preference. A user cannot accidentally hide rehearsal
labelling. This is enforced by declaring `--_demo-*` in the raw scale
and never remapping them in the dark-mode stub.

---

## 10. Role badge styles

Six roles. Each has a distinct hue family (not colour alone — a small
icon also accompanies each badge).

| Token | Hex | Role | Icon |
|---|---|---|---|
| `--role-owner` | `#1D4ED8` | Owner | `crown` (Lucide) |
| `--role-admin` | `#6D28D9` | Admin | `shield` |
| `--role-team-lead` | `#0F766E` | Team Lead | `users` |
| `--role-agent` | `#374151` | Agent | `user` |
| `--role-viewer` | `#4B5563` | Viewer | `eye` |
| `--role-orvn` | `#B91C1C` | ORVN Staff | `building` |

All values pass 4.5:1 contrast against white. Role badges render as
`--radius-pill` chips with `--text-micro` and `--fw-medium`.

---

## 11. Forbidden visual patterns

The following are banned across all PAS surfaces. Any PR that
introduces these should be rejected at review:

| Pattern | Why forbidden |
|---|---|
| AI purple/pink gradients | Positions PAS as AI product, not operations software |
| Neon, vaporwave, cyberpunk colours | Wrong mood for daily-use ops software |
| Glassmorphism / backdrop-filter > 4px blur | Obscures contrast, fails accessibility |
| Neumorphism | Trades legibility for novelty |
| Emoji as icons | Non-accessible; screen readers read them unpredictably |
| Cute illustrations in empty states | Empty states are operational facts, not marketing |
| Bright red for anything other than Critical + Destructive | Severity inflation |
| Brand colour as a gradient | Collapses brand identity; reads as AI product |
| Animations > 300ms (except `--anim-presence`) | Feels sluggish; operational calm |
| Bounce / spring / overshoot easing | "Theme park, not calm partner" |
| More than 3 font weights simultaneously | Visual noise, hierarchy collapse |
| Modals for non-destructive confirmation | Use inspectors / drawers instead |
| CSS `width`/`height` transitions | Layout thrash |
| `color` as the only distinguishing signal | Fails colour-blind users |

---

## 12. How tokens support operational calm and customer experience

The token system is designed so that users end the day thinking
*"I had help today"* rather than *"I'm exhausted from the tool."*
Specific mechanisms:

**Neutral scale with blue undertone** — the subtle cool tint is never
consciously noticed, but it prevents the eye-fatigue of warm-gray
dense interfaces. A brokerage owner scanning leads for 6 hours needs
a surface that doesn't accumulate visual debt.

**Brand used sparingly** — `--brand` appears in at most two places per
screen (primary CTA + one accent). When the operator sees that blue,
they know something is actionable. The signal is consistent.

**Severity as a meaningful system** — five hue families, not "three
shades of red." An operator trained on PAS knows instantly that amber
= attention, deep crimson = stop and act. Severity inflation (the
leading cause of dashboard fatigue) is structurally prevented.

**Demo labelling in immutable amber** — operators never misread
rehearsal data as live data. Trust is architectural, not policy.

**Motion that conveys causality** — drawers enter from the side that
produced them. Panels animate with `--ease-out` (fast in, slows to
rest — feels responsive and stable). No motion is decorative.

**Three type weights, not twelve** — reading hierarchy is established
by size and colour, not weight variety. The eye finds what it needs
without scanning through competing levels of emphasis.

---

## 13. Dark mode placeholder

Dark theme ships in v1.x after a dedicated visual QA pass.

Pre-defined token pairs (to be activated in v1.x):

```
surface-base.dark    ← --_n-950 (#0B0B11)
surface-raised.dark  ← --_n-900 (#111118)
ink-primary.dark     ← --_n-50  (#F6F6FB)
ink-secondary.dark   ← --_n-200 (#DCDCE8)
border.dark          ← --_n-700 (#2A2A3A)
brand.dark           ← --_br-300 (#8FA8F7)  [lighter for dark bg contrast]
signal-urgent.dark   ← TBD — amber needs revalidation on dark surface
signal-critical.dark ← TBD — crimson needs revalidation on dark surface
```

The `--_demo-*` tokens are NOT remapped in dark mode (the immutability
rule applies regardless of theme).

The dark mode block in `globals.css` is an intentionally empty
`@media (prefers-color-scheme: dark) :root {}` — browsers will not
auto-darken any surface.

---

## 14. Changes from Step 1

| Token | Step 1 value | Step 2 locked value | Reason |
|---|---|---|---|
| `--brand` | `#5B3FD4` | `#3B52D4` | Hue shift 260°→232°; away from AI purple, toward operational authority |
| `--surface-base` | `#F8F8FC` | `#F6F6FB` | Cooler undertone to match new neutral scale |
| `--ink-primary` | `#111111` | `#111118` | Minimal blue tinge added to harmonise with scale |
| `--_n-*` (scale) | Ad-hoc values | Full 14-step custom cool-gray | Proper systematic scale with blue undertone |
| `--signal-fyi` | `#6B7280` (warm gray) | `#3D5A6C` (cool slate) | Distinct from ink-muted; clear FYI identity; 6.8:1 contrast |
| `--signal-approval` | `#5B3FD4` (old brand) | `#3B52D4` (new brand) | Tracks brand shift |
| `--ls-*` | Missing | Added to all type tokens | Letter-spacing is part of the typographic system |
| Semantic aliases | None (raw values only) | `--ink-*`, `--surface-*`, etc. | Dark-mode readiness; one remap layer |
| Shadow colour | `rgba(20,22,24,…)` | `rgba(13,13,20,…)` | Matches neutral scale undertone |
