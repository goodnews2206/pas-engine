# PAS Design System Definition

> Status: draft v1. Owner: ORVN Labs. Last updated: 2026-05-25.
> Sibling to `docs/pas_uiux_reference_study.md` (reconciliation
> against `ui-ux-pro-max`) and the four product/architecture docs.
> Defines the *tokens, behaviours, and craft floor* every PAS surface
> obeys. **No frontend code yet.**

## 0. Scope

This document defines design **tokens** (numbers, names, scales) and
**behaviour contracts** (how a component must behave to count as a
PAS component). It does not pick specific hex values for the
signature palette beyond named role intent; those land in v1.x with
sign-off. It does pick everything *structural*: scale, rhythm,
density, motion, accessibility, severity semantics.

The pre-delivery checklist at the end (§28) is the floor. A surface
that does not pass it cannot ship.

---

## 1. Typography system

### 1.1 Family

- **Primary UI:** a geometric humanist sans (e.g. Inter). Open
  apertures, neutral, screen-optimised. Variable font preferred for
  weight + optical-size control.
- **Mono:** a humanist mono (e.g. JetBrains Mono / Geist Mono /
  Berkeley Mono) for transcripts, audit logs, evidence payloads,
  numbers in tables.

Concrete family choices are validated in v1.x. The structural rules
below are independent of family.

### 1.2 Type scale

A 1.125 (major second) scale, snapped to 4-pt grid:

| Token | Size | Line-height | Weight | Use |
|---|---|---|---|---|
| `display` | 32 | 40 | 600 | Page H1 (rare; reserved for surfaces like onboarding). |
| `title` | 24 | 32 | 600 | Module title. |
| `subtitle` | 18 | 28 | 600 | Section heading inside a module. |
| `body-lg` | 16 | 24 | 400 | Default body, table cell. |
| `body` | 14 | 20 | 400 | Secondary text, labels. |
| `caption` | 12 | 16 | 400 | Metadata, timestamps, helper text. |
| `micro` | 11 | 16 | 500 | Tag, badge, chip. Use sparingly. |

**Maximum three weights in active use** at any time: 400, 500, 600.
700 only for the single signature brand mark; not for body or UI.

### 1.3 Typographic rules

- Never go below `caption` (12 px) for primary information.
- Numbers in tables are tabular-numeric. Always.
- Timestamps render as absolute on hover and relative inline ("2h
  ago / 14:02 UTC").
- No italics for emphasis in UI chrome. Italics reserved for
  proper nouns inside transcripts.
- Sentence case for buttons and labels ("Approve recommendation",
  not "Approve Recommendation").
- Title case for module names in the sidebar ("Action Proposals").

---

## 2. Spacing system

8-point baseline. Tokens:

| Token | px | Use |
|---|---|---|
| `space-0` | 0 | No gap. |
| `space-hair` | 4 | Inside chips, between icon + label, divider gaps. |
| `space-xs` | 8 | Tight inline rhythm. |
| `space-sm` | 12 | Comfortable inline rhythm. |
| `space-md` | 16 | Card inner padding, default form gap. |
| `space-lg` | 24 | Section spacing, card-to-card. |
| `space-xl` | 32 | Module gutter (desktop), large section break. |
| `space-2xl` | 48 | Page top breathing room, hero surfaces. |
| `space-3xl` | 64 | Onboarding, empty-page sky. |
| `space-4xl` | 96 | Rare; full-bleed page anchor. |

**Outer module gutters:** desktop 32, tablet 24, mobile 16.

---

## 3. Radius system

| Token | px | Use |
|---|---|---|
| `radius-none` | 0 | Tables, full-bleed surfaces. |
| `radius-xs` | 4 | Chips, badges, inline tags. |
| `radius-sm` | 6 | Inputs, buttons, dense cards. |
| `radius-md` | 10 | Cards, drawers (inner). |
| `radius-lg` | 14 | Panels, modal frames, drawers (outer). |
| `radius-pill` | 999 | Avatars, status dots, severity chips. |

No radius greater than 14 px for rectangular surfaces. Larger radius
reads as marketing-page, not operations software.

---

## 4. Elevation system

PAS uses *four* elevation tiers, not eight. More tiers = visual noise.

| Tier | Use | Treatment |
|---|---|---|
| `surface-base` | Page background. | Flat. |
| `surface-raised` | Cards, panels, sidebar. | Subtle shadow + 1 px hairline border. |
| `surface-overlay` | Drawers, peek pane. | Stronger shadow + hairline. |
| `surface-popover` | Menus, command palette, tooltips, severity toasts. | Hairline + soft drop shadow + slight backdrop blur (≤4 px). |

Elevation never relies on shadow alone — there is always a hairline
border at the same depth for users with low contrast or reduced
motion.

---

## 5. Shadows

Two shadows, no more:

| Token | Spec (light theme baseline) |
|---|---|
| `shadow-soft` | `0 1px 2px rgba(20, 22, 24, .04), 0 1px 1px rgba(20, 22, 24, .03)` |
| `shadow-overlay` | `0 8px 24px rgba(20, 22, 24, .08), 0 2px 6px rgba(20, 22, 24, .04)` |

Dark theme remaps with reduced intensity (shadows are nearly
invisible on dark surfaces; a subtle inset hairline replaces them).

No coloured shadows. No glow effects.

---

## 6. Animation timing

| Token | Duration | Easing | Use |
|---|---|---|---|
| `anim-instant` | 80 ms | linear | Microstate (hover, press). |
| `anim-fast` | 150 ms | ease-out | Default entrances. |
| `anim-base` | 200 ms | ease-in-out | Drawer / peek / inspector. |
| `anim-slow` | 300 ms | ease-in-out | Severity surfacing, banner reveal. |
| `anim-presence` | 1200 ms | ease-in-out, infinite, opacity-only | "PAS is thinking" indicator. |

No keyframe is longer than 300 ms except `anim-presence`. No bounce,
no spring, no overshoot.

**`prefers-reduced-motion: reduce` collapses every animation to a
50 ms opacity fade.** `anim-presence` stops entirely; presence shows
as a static "Thinking…" label.

---

## 7. Transition rules

- **Cause and effect.** A drawer enters from the side that produced
  it (right pane peek = right side; bottom approval = bottom).
- **Co-located changes batch.** Inserting a row + updating a count
  animate together, not sequentially.
- **No layout-thrash transitions.** Use opacity + transform, not
  width / height.
- **Loading does not flash.** A skeleton displays only after a
  100 ms threshold; faster responses snap directly to content.

---

## 8. Grid system

- **Desktop:** 12-column grid, 24 px gutter, max content width 1400
  px centered, min content width 1024 px.
- **Tablet (768–1023):** 8-column grid, 20 px gutter.
- **Mobile (≤767):** 4-column grid, 16 px gutter.
- **Sidebar reserve:** 256 px expanded, 64 px collapsed.

Modules are built on top of this grid; deviations require an
explicit pattern note (e.g. Simulation Lab can run full-bleed for
scenario rendering).

---

## 9. Sidebar behaviour

- **States:** expanded (256 px) and collapsed (64 px, icon-only).
- **Default:** expanded on ≥1280 px viewports, collapsed below.
- **Family headers:** never empty. Hide the whole family if no
  module is visible to the role.
- **Active item indication:** left rail accent (3 px) + bold weight
  + background tint. Never both icon-color and bold and background —
  one signal at a time.
- **Sub-routes:** indented to 12 px under their parent; reveal on
  parent active only.
- **Footer slot:** user identity, tenant name, account menu. ORVN
  tenant switcher appears here for ORVN role only.
- **Keyboard:** Cmd/Ctrl+`B` toggles sidebar; Tab order walks the
  visible items only.

---

## 10. Panel behaviour

PAS has four panel kinds:

| Panel | Width / behaviour |
|---|---|
| **Peek pane** | 360 px right side; can stack on top of inspector when both are open (peek on top). Closes on `Esc`. |
| **Inspector** | 420 px right side; slides over the main content; preserves scroll on the underlying module. Closes on `Esc` (after peek). |
| **Approval drawer** | 480 px right side; **stacks above peek + inspector** when an approval is invoked from either. Closes on `Esc` or explicit decision. |
| **Modal** | Centered, max 640 px; reserved for confirmation of irreversible actions only. Esc closes unless the action requires explicit choice. |

Panels never trap focus silently — focus management is part of the
spec, not an afterthought.

---

## 11. Command surfaces

### 11.1 Top bar

- 56 px tall, full width.
- Left: tenant context strip (when scope ≠ default).
- Center: command bar entry (Cmd/Ctrl+K).
- Right: presence indicator, notifications bell, profile menu.

### 11.2 Command bar (Cmd/Ctrl+K)

- Opens a popover panel at the top of the viewport.
- **Single input** that does three things in parallel:
  1. Module/route search.
  2. Recent items / pinned items.
  3. PAS composer entry (Enter to send to PAS; Tab to swap modes).
- Closes on `Esc` or click-outside.

### 11.3 PAS composer (dockable, bottom)

- Default position: pinned to the bottom of every dashboard page,
  full width, 56 px collapsed / up to 200 px expanded.
- Submits on Enter; Shift+Enter inserts a newline.
- Mode toggle (Cmd/Ctrl+K opens command bar from composer; explicit
  send routes to PAS).
- Visual state mirrors PAS presence: "PAS is observing" / "PAS is
  thinking" / "PAS is waiting on you".

---

## 12. Cards

| Property | Spec |
|---|---|
| Padding | `space-md` (16) on mobile, `space-lg` (24) on desktop. |
| Radius | `radius-md` (10). |
| Background | `surface-raised`. |
| Border | 1 px hairline + `shadow-soft`. |
| Title | `subtitle`, weight 600. |
| Body | `body` (14). |
| Action area | Bottom-right; at most two primary actions + a single "ask PAS" affordance. |
| Evidence link | Inline anchor near the claim — never a separate "details" button. |
| Severity treatment | A left-rail accent (3 px) in the severity colour; no background tint. |

Cards never carry two competing CTAs of equal weight.

---

## 13. Tables

- **Header:** sticky on vertical scroll; 40 px tall; weight 500;
  caption-sized labels.
- **Row height:** 48 (comfortable) / 36 (compact).
- **Columns visible by default:** ≤7. The rest collapse into the
  inspector.
- **Sort:** clickable header; arrow indicator; secondary sort allowed
  with Shift-click.
- **Filter:** chip rail above the table; named filters retain via
  URL state.
- **Selection:** checkbox column (left); bulk action bar appears
  above the table only when ≥1 row is selected.
- **Empty:** copy block per Product Design Book §8.2, never a
  spinner trapped in the table.
- **Row click:** opens the inspector; double-click is not a primary
  affordance.

---

## 14. Approval drawers

- 480 px wide; right side; stacks above peek + inspector.
- Header: action title + severity chip + expiry countdown.
- Body: evidence panel, scope panel, side-effects panel, reversal
  note ("Reversible" / "Irreversible — second confirm required").
- Footer (sticky): **Approve** (primary) · **Decline** (secondary)
  · **Ask PAS** (ghost) · "Set quiet hours" (link).
- Approve requires a reason only when the proposal declares "high
  impact" or the user role is "default-deny-on-write"-tier.
- Lapse: when the TTL hits 0, the drawer transitions to "Expired
  without decision" copy and an audit link.

---

## 15. Alert banners

Module-level inline alerts. Three banner shapes:

| Banner | Use | Treatment |
|---|---|---|
| `banner-info` | FYI module note (rare). | Hairline + small left icon, no background. |
| `banner-warn` | Stale data, integration degraded, partial sync. | Soft warn-tone background; left-rail accent. |
| `banner-critical` | Compliance / integrity / outage. | Strong tone; persistent; dismiss requires explanation. |

Banners do not overlap with notifications — they live inside the
module, not the global notification surface.

---

## 16. PAS communication surfaces

### 16.1 Composer (persistent bottom)

- Collapsed: 56 px tall, single-line input, presence indicator on
  the right.
- Expanded: up to 200 px with multi-turn preview of the last 3
  replies above the input.

### 16.2 Peek pane (right side, contextual)

- 360 px wide; sticky to the right; scrolls independently of the
  main module.
- Header: thread title + close (Esc) + expand to full thread.
- Body: bubble-less thread (PAS = full-width block, user =
  right-aligned with subtle indent). No avatar bubbles.
- Inline embeds: when PAS pulls a section ("show today's
  callbacks"), the embed renders inside the thread with the same
  card spec as the real module — not a stripped preview.

### 16.3 Full thread (route)

- Dedicated route, shareable inside the workspace.
- Pinned answers section at top; chronological thread below.
- Evidence anchors render with their source module name.

---

## 17. Empty states

- Centered block, 48 px from top edge.
- Stack: small icon (24 px, no decoration) → headline (`subtitle`)
  → copy (`body`, 1–2 sentences) → primary action.
- Copy follows Product Design Book §8.2 ("Nothing here yet…").
- **No illustrations.** Empty is a fact, not a marketing moment.

---

## 18. Loading states

| State | Treatment |
|---|---|
| Known shape, fast (<100 ms) | Snap to content; no skeleton. |
| Known shape, slow (≥100 ms) | Skeleton in the exact shape of the result. |
| Unknown shape | A calm progress indicator with a label ("Loading audit log…"). |
| PAS thinking | "PAS is thinking" pill with the slow opacity-pulse `anim-presence`. |
| Streaming response | Token-level append in the composer / peek; no jitter. |

No indeterminate spinner anywhere a skeleton can be used.

---

## 19. Notification styling

Per Notification Architecture, five severities. Visual treatment:

| Severity | Colour role | Icon | Position-of-honour |
|---|---|---|---|
| FYI | `signal-fyi` (neutral cool) | `info` (Lucide) | In-app feed only. |
| Needs Attention | `signal-attention` (warm) | `bell` | Bell drawer + Command Center. |
| Urgent | `signal-urgent` (amber) | `alert-triangle` | Bell + toast + Command Center. |
| Approval Required | `signal-approval` (brand-adjacent calm) | `check-circle` | Bell + approval drawer trigger. |
| Critical | `signal-critical` (deep crimson, not bright red) | `alert-octagon` | Bell + persistent banner + push. |

Severity colour is **always paired with an icon and a position**.
Colour alone is never the only signal (colour-vision support).

---

## 20. Mobile responsive rules

- Breakpoints: 375 / 768 / 1024 / 1440 (adopted from `ui-ux-pro-max`).
- Below 768: single-column module layout; sidebar replaced by
  bottom tab bar + "More" sheet.
- 768–1023: two-column where useful (e.g. Calls list + transcript);
  sidebar collapsed by default.
- 1024–1439: full sidebar; main + optional peek pane.
- ≥1440: full sidebar + main + peek + inspector concurrently
  (approval drawer stacks above all).

- Touch targets ≥44×44 dp on mobile, ≥32×32 dp on desktop for
  non-primary controls.
- No mobile-only or desktop-only modules (mobile may "hand off to
  desktop" for v1, but the route is the same).

---

## 21. Accessibility rules

- **WCAG 2.2 AA floor.** Contrast 4.5:1 for text; 3:1 for UI
  controls and meaningful icons.
- **Focus visible** on every focusable element. Focus ring 2 px,
  `signal-approval`-adjacent calm hue, 2 px offset.
- **Keyboard reaches everything.** Cmd/Ctrl+K command bar; Esc
  closes from the topmost panel inward.
- **Screen reader:** all interactive elements have accessible names;
  severity badges have text equivalents; live regions for
  notifications.
- **`prefers-reduced-motion: reduce`** is the floor — when set, only
  opacity fades remain.
- **No colour-only signals.** Severity, status, demo, and validity
  all pair colour with an icon and a position.
- **Tab order matches reading order.** Always.

---

## 22. Dark / light behaviour

- **Light is the default.** Day-time defaults for daily-use ops
  software.
- **Dark ships in v1.x.** Tokens are pre-defined; activation comes
  with the dark-theme QA pass.
- **System preference is respected** when a user has not chosen.
- **No "AMOLED" pure-black mode** in v1.x; dark uses a near-black
  surface to avoid haloing.

Tokens are paired:
```
surface-base.light  ↔ surface-base.dark
ink-primary.light   ↔ ink-primary.dark
…
```

---

## 23. Interaction states

Every interactive element declares five states:

| State | Treatment |
|---|---|
| default | Resting. |
| hover | Subtle tint shift + cursor change. |
| active (pressed) | Slightly darker tint + 1 px down shift (optional). |
| focus-visible | 2 px focus ring + offset. |
| disabled | Reduced opacity (60%) + cursor `not-allowed` + ARIA-disabled. |

Loading state on an action is a sixth state: spinner replacing the
label, button width preserved, no layout shift.

---

## 24. Destructive-action styling

- **Colour:** `action-destructive` (deep crimson tone — same family
  as `signal-critical` but distinct token).
- **Confirmation required** for every destructive action. Use a
  **modal** (not a drawer) because the user must commit or cancel.
- **Reversibility note in the modal.** "Cannot be undone" if true;
  otherwise list the reversal path.
- **Never primary by default.** A destructive button is secondary
  unless the entire surface is dedicated to destruction (e.g. a
  "delete tenant" admin page).

---

## 25. Severity colour system

Five tokens, mapped to the five severity levels (Notification
Architecture §2):

| Token | Severity | Intent |
|---|---|---|
| `signal-fyi` | FYI | Cool neutral; whisper, not shout. |
| `signal-attention` | Needs Attention | Warm hue; reads "look, when convenient". |
| `signal-urgent` | Urgent | Amber; reads "now-ish". |
| `signal-approval` | Approval Required | Brand-adjacent calm; reads "your call". |
| `signal-critical` | Critical | Deep crimson; reserved; reads "right now". |

Concrete hex values land in v1.x. The rule: each must pass 4.5:1
against `surface-base` (light) and against `surface-base.dark`.

---

## 26. Demo / rehearsal labeling

Demo state is **structurally distinct from severity**. Three places
demo appears:

| Surface | Treatment |
|---|---|
| Site-wide rehearsal banner | Persistent top strip; `demo` token (distinct from all severity tokens). Copy per Design Book §8.5. |
| Inline artifact tag | Pill with "Simulated"; `radius-pill`; muted demo tone; placed adjacent to the title or row identifier. |
| PAS speaking inside rehearsal | First reply includes the rehearsal disclosure (Design Book §8.5). |

The demo token must be **non-removable** by user theme preference.
A user cannot accidentally hide rehearsal labelling.

---

## 27. Role-badge styling

- Pill (`radius-pill`), `micro` type, 4-pt vertical padding.
- Six tokens, one per role: `role-owner`, `role-admin`,
  `role-team-lead`, `role-agent`, `role-viewer`, `role-orvn`.
- Treatments use saturation + label, not colour alone (e.g.
  Read-only Viewer also carries an `eye` icon at all sizes).
- Role badges appear next to the user identity in the top-bar
  profile menu, in audit log entries, and in approval drawers.

---

## 28. Density scaling rules

- **Two densities, no more:** comfortable (default), compact.
- **Set per user** in Settings; saved to profile.
- **Applies to:** table row height, card padding, sidebar item
  height, composer height.
- **Does not apply to:** typography scale, animation timing,
  severity colours, demo labelling. Those are invariants.

---

## 29. Pre-delivery checklist

A surface ships only when every box is true:

- [ ] Uses only tokens from this doc; no ad-hoc hex / px values.
- [ ] Passes WCAG 2.2 AA on contrast (4.5:1 text / 3:1 UI).
- [ ] Has visible focus state on every focusable element.
- [ ] Supports `prefers-reduced-motion: reduce`.
- [ ] Keyboard reaches every interactive element in reading order.
- [ ] No emoji used as an icon anywhere.
- [ ] `cursor-pointer` on every clickable element.
- [ ] Empty, loading, error, and success states all designed.
- [ ] Demo / rehearsal labelling is correct when applicable.
- [ ] Severity colours paired with icon + position.
- [ ] Mobile (375 / 768) rendered and validated.
- [ ] Three weights max in active use; sentence case for buttons.
- [ ] No more than two primary CTAs per card / module.
- [ ] No layout-thrash animations.
- [ ] No raw token / secret / internal ID visible on the surface.
- [ ] Demo banner cannot be hidden by user theme.

---

## 30. Open design-system questions

- **Signature hue.** A single confident brand colour, or near-
  neutral with rhythm as identity?
- **Mono family.** JetBrains Mono vs Geist Mono vs Berkeley Mono.
  Licensing + readability tradeoffs.
- **Variable font** vs static cuts — disk weight vs control.
- **Severity dark-mode mapping.** Amber and crimson read very
  differently on dark surfaces; specific dark hex pairings still
  open.
- **Approval drawer + inspector + peek** stacking ergonomics on
  1280–1439 viewports; may need a soft-collapse heuristic.
- **Composer height behaviour** during long PAS replies — does it
  expand inline, or always reveal in peek pane?
- **Notification toasts**: do they ever appear, or is the bell + in-
  app feed the only path? Current draft says "rarely" but leaves it
  open.

---

*End of v1.*
