# PAS301.5 — Authentication Strategy Decision

> Status: decision document (planning only — no code, UI, backend, CORS, auth implementation, or package changes).
> Owner: ORVN Labs.
> Anchored on: `main` @ `8e9b237`, with PAS301 authored on branch `pas301-identity-ownership-session-workspace-lifecycle`.
> Decides: PAS301 §9/§26 open question — which authentication direction PAS commits to before PAS301A implementation begins.
> Naming: **PAS = Proactive Assistant for Scale.**

---

## 1. Purpose

PAS301 defined identity, ownership, session, and workspace lifecycle, and deliberately left one
question open (PAS301 §26): *which authentication method does PAS lead with?* That question must
be answered before PAS301A (Account/Profile Shell) and especially PAS301D/E (auth provider and
sign-in flow) can proceed, because the choice shapes the account model, the session direction,
the integration roadmap, and the first thing every user touches.

This document evaluates five candidate strategies against ten criteria, makes a decision, and
specifies the resulting sign-in/sign-up UX direction. It is **planning/spec only** — it
implements no auth, touches no UI, backend, CORS, or packages, and does not push.

The decision is read against PAS300/PAS301 doctrine: auth must feel **welcome home, simple,
fast, secure, non-enterprise-clunky, safe for agents, reassuring for brokerages** — and must
never make the user think about authentication (PAS301 §29).

---

## 2. Options under evaluation

1. **Email + password** — classic credentials stored and verified by PAS.
2. **Magic link** — passwordless; a one-time secure link emailed on each sign-in.
3. **Google sign-in** — OAuth/OIDC against Google identity.
4. **Google-first with magic-link fallback** — Google as the primary path, magic link for
   non-Google users.
5. **Future SSO / enterprise auth** — SAML/OIDC against a brokerage/enterprise IdP.

---

## 3. Evaluation criteria

Each option scored against: agent onboarding friction · broker owner onboarding friction ·
trust · security · support burden · workspace switching fit · Google integrations fit · future
enterprise fit · speed to build · risk. (Workspace switching fit is constant across options —
switching is in-session re-scoping per PAS301 §7 and never re-authenticates — so it favors any
option that keeps sessions clean; noted per option only where it differs.)

### Option 1 — Email + password
- **Agent onboarding friction:** Medium–high. New credential to create and remember; a
  password manager helps, many agents don't use one.
- **Broker owner onboarding friction:** Medium. Same friction, on a less price-sensitive user.
- **Trust:** Neutral-to-negative. "Another password to manage" is fatigue, not delight.
- **Security:** Weakest by default. PAS becomes a credential custodian — hashing, breach
  exposure, reuse across sites, phishing, reset flows. Largest attack surface.
- **Support burden:** Highest. Password resets, lockouts, "I forgot," reset-email deliverability
  — the dominant auth support cost in most products.
- **Workspace switching fit:** Neutral.
- **Google integrations fit:** None. A separate password gives PAS no path to Gmail/Calendar/Drive.
- **Future enterprise fit:** Poor. Enterprises want SSO, not local passwords.
- **Speed to build:** Medium. Looks simple, but secure password handling (hashing, reset,
  rate-limiting, breach checks) is real work.
- **Risk:** High — security surface + support cost + zero integration leverage.

### Option 2 — Magic link
- **Agent onboarding friction:** Low. Enter email, click link. Nothing to create or remember.
- **Broker owner onboarding friction:** Low.
- **Trust:** Positive. No password to lose; feels modern and calm.
- **Security:** Good. No stored passwords; security rides on email-account security and link
  hygiene (short expiry, single use, anti-replay).
- **Support burden:** Low–medium. No resets; the cost shifts to email deliverability and
  "link expired / went to spam."
- **Workspace switching fit:** Good — clean sessions, no per-switch friction.
- **Google integrations fit:** None directly. Authenticating by email does not grant
  Gmail/Calendar/Drive scopes.
- **Future enterprise fit:** Neutral. Coexists with SSO; not itself enterprise.
- **Speed to build:** Medium. Needs reliable transactional email + secure token handling.
- **Risk:** Medium — primarily email deliverability and link-handling correctness.

### Option 3 — Google sign-in
- **Agent onboarding friction:** Lowest. One tap with an account the agent already has; no new
  credential, no email round-trip.
- **Broker owner onboarding friction:** Lowest. Same one-tap.
- **Trust:** High *for Google users* — familiar, reputable, no new secret. Slightly lower for
  the minority who avoid Google or use a non-Google work email.
- **Security:** Strong. Google handles credentials, MFA, and breach response; PAS never stores a
  password. Offloads the hardest part of auth to a hardened provider.
- **Support burden:** Lowest. Effectively no reset/lockout flows owned by PAS.
- **Workspace switching fit:** Good — clean OIDC session; switching stays in-session.
- **Google integrations fit:** **Best.** The same identity is the on-ramp to incremental Gmail,
  Calendar, and Drive scopes PAS's roadmap needs — auth and integration share a provider.
- **Future enterprise fit:** Good. Google Workspace is itself an enterprise IdP; many brokerages
  run on it.
- **Speed to build:** Fast. Mature OIDC libraries and provider tooling.
- **Risk:** Medium-low — provider dependency, and the non-Google minority needs a fallback.

### Option 4 — Google-first with magic-link fallback
- **Agent onboarding friction:** Lowest for the Google majority; low for the rest.
- **Broker owner onboarding friction:** Lowest / low, same split.
- **Trust:** High across the board — one-tap for Google users, passwordless for everyone else.
- **Security:** Strong. No PAS-stored passwords on either path; credentials handled by Google or
  by short-lived single-use links.
- **Support burden:** Low. No password resets; residual cost is link deliverability for the
  fallback minority.
- **Workspace switching fit:** Good — both paths yield clean sessions.
- **Google integrations fit:** Best — preserves the Google on-ramp for the majority while not
  excluding anyone.
- **Future enterprise fit:** Good — leaves room to add SSO without reworking the model.
- **Speed to build:** Fast–medium. Google OIDC plus a magic-link path; both are well-trodden.
- **Risk:** Low — diversified across two passwordless paths, no credential custody, full
  coverage.

### Option 5 — Future SSO / enterprise auth
- **Agent onboarding friction:** N/A for self-serve agents; SSO is org-mediated.
- **Broker owner onboarding friction:** High up front — IdP configuration, metadata, IT
  involvement. Low afterward for users.
- **Trust:** High in enterprise contexts (expected and required).
- **Security:** Strong; centralized enterprise control.
- **Support burden:** High to set up per tenant; low steady-state.
- **Workspace switching fit:** Compatible.
- **Google integrations fit:** Indirect.
- **Future enterprise fit:** Essential *eventually* — large brokerages will require it.
- **Speed to build:** Slow. Per-IdP configuration, testing, support.
- **Risk:** High cost/complexity now, low value now — it serves a customer segment PAS is not
  yet selling to. Premature.

---

## 4. Decision

**Primary: Google sign-in.**
**Fallback: email magic link.**
**Later (only if needed): password and/or enterprise SSO.**

This is Option 4, with Option 5 explicitly deferred and Option 1 explicitly rejected as a
launch path.

### Why

- **Agents already live in Google.** Most real-estate agents run their working lives on a Gmail
  address; one-tap sign-in removes the single biggest onboarding drop-off — creating and
  remembering yet another password.
- **Brokerages use Gmail, Calendar, and Drive.** The buyer's existing stack is Google; signing
  in with it is familiar and lowers the broker-owner friction too.
- **PAS's future requires Gmail/Drive/Calendar integrations.** The Brain (PAS306), callbacks,
  and document ingestion all point at Google data. Authenticating with Google lets PAS request
  those scopes *incrementally* on the same identity — auth and integration share one provider
  instead of bolting integration on later.
- **Google reduces onboarding friction** to its theoretical minimum (one tap) and offloads the
  hardest, riskiest parts of auth — credential storage, MFA, breach response — to a hardened
  provider.
- **Magic link covers non-Google users** without forcing a password, so no one is excluded and
  the passwordless, calm posture is preserved for everyone.
- **Password-first creates unnecessary support burden** — resets, lockouts, reset-email
  deliverability, and a credential-custody security surface — for zero integration benefit. PAS
  declines to be a password custodian at launch.

### Rejected options
- **Email + password (Option 1)** — rejected as a launch path: highest support burden, largest
  security surface, no Google integration leverage. May return *later* only as a narrow
  accommodation if a real user segment cannot use Google or magic link.
- **Magic link alone (Option 2)** — good, but as the *only* method it forgoes the Google
  one-tap and, critically, the integration on-ramp. Kept as the fallback, not the primary.
- **Google alone (Option 3)** — strong, but excludes the non-Google minority and lacks a
  graceful path for them; pairing it with magic link closes that gap.
- **Enterprise SSO (Option 5)** — deferred. Essential eventually for large brokerages, but
  premature now: high per-tenant cost serving a segment PAS isn't selling to yet. The model
  leaves room for it (PAS301 §9) without building it.

---

## 5. Sign-in UX recommendation

- **Primary affordance:** a prominent **"Continue with Google"** button — the visual default.
- **Secondary affordance:** **"Sign in with email"** (magic link) directly beneath, equal in
  legitimacy, smaller in emphasis.
- **No password field on the default screen.** Email entry leads to "we'll send you a secure
  link," not a password prompt.
- **One identity, many doors.** Sign-in authenticates the *person*; it never asks "which
  workspace" — workspace context resolves after sign-in (PAS301 §§7, 9).
- **Copy:** *"Sign in to your PAS."* · *"Continue with Google"* · *"Or get a secure sign-in
  link by email."*
- **Failure states:** expired/used link → one-tap re-request; Google denied/cancelled → fall
  back to email link without dead-ending; unknown email → offer sign-up without confirming
  whether the address exists (anti-enumeration).

## 6. Sign-up UX recommendation

- **Same two affordances** as sign-in — sign-up and sign-in are one unified entry; PAS detects
  new vs returning rather than making the user choose.
- **Minimal fields.** Google provides name and email; magic-link sign-up asks only email + name.
- **No org questions at sign-up.** A Personal Agent Workspace is created automatically
  (PAS301 §8A); brokerage/team come later or via invite.
- **No integration scope requests at sign-up.** Sign-in scope is identity only; Gmail/Calendar/
  Drive scopes are requested *incrementally and in context*, when a feature needs them — never
  as a wall at the door.
- **Copy:** *"Meet your PAS — this stays with you no matter where you work."*

## 7. First login experience

- Land in the new **Personal Agent Workspace** → straight into a warm first-run (PAS301 §8A):
  "What should I call you, and what do you want to call me?" then one useful first action.
- **No setup gauntlet, no scope wall.** Welcome home, not configuration.
- Integration connection (Google data) is *offered* later, in context, with clear value — not
  required to start.

## 8. Returning login experience

- Sign in (one tap for Google, one link for email) → land in the **last active workspace**
  (PAS301 §8E).
- No re-onboarding, no re-consent, no repeated setup. *"Welcome back. Here's what needs you
  today."*

## 9. Invited user flow

- Invitation by email (PAS301 §14). The accept screen names the inviting workspace and the role.
- **Already has a PAS account:** the invite attaches to the existing identity — one identity,
  additional door; no duplicate account regardless of which auth method they use.
- **No account yet:** unified Google/magic-link sign-up precedes acceptance; their Personal
  Workspace is created alongside, and accepting adds the brokerage/team seat without exposing
  the personal workspace.
- **Auth-method independence:** the invited email and the chosen sign-in method need not match
  provider (an invite to a Gmail address can still be accepted via magic link, and vice versa),
  as long as the verified identity resolves to that email.

## 10. Solo agent flow

- The default and most important path. Google one-tap (or magic link) → Personal Workspace →
  immediate value. No brokerage, no billing, no integration required to begin (PAS301 §16).
- This is the bottoms-up adoption funnel; auth friction here is the funnel's top, so it is
  minimized hardest.

## 11. Brokerage owner flow

- Owner signs in the same way (Google preferred — brokerages run on Workspace) → creates a
  Brokerage Workspace (PAS301 §8C) → invites agents.
- Invited agents arrive via §9; each keeps a private Personal Workspace.
- Google-based identity smooths later Workspace-wide integration and (eventually) SSO.

---

## 12. Session implications

- **Both paths yield clean sessions** that fit PAS301 §11: idle + absolute timeouts, remember-
  device, bounded concurrent sessions, server-side invalidation on sign-out.
- **Google (OIDC):** PAS holds its own session after verifying the Google identity; PAS session
  lifetime is independent of Google's, so PAS controls timeout/revocation.
- **Magic link:** establishes the same PAS session after link verification; identical
  session behavior thereafter.
- **Token/cookie direction** (httpOnly, secure, same-site; access+refresh) is decided in
  PAS301D/F, unchanged by this choice — both methods feed the same session boundary.
- **Step-up re-auth** for high-risk actions (PAS301 §11) works with both (re-prompt Google, or
  re-send a link).

## 13. Workspace switching implications

- **Switching never re-authenticates** (PAS301 §7) regardless of sign-in method — it re-scopes
  authorization within the live PAS session. The auth choice does not touch switching.
- **One identity across methods:** whether the person signed in via Google or magic link, they
  hold one identity and one switcher; the method is invisible after sign-in.
- A user must not end up with *two* identities by signing in via Google once and magic link
  another time on the same email — both must resolve to the same identity (account-linking
  rule; see risks).

---

## 14. Risks and mitigations

- **Non-Google users excluded** → *Mitigation:* magic-link fallback as a first-class,
  equal-legitimacy path; no one is forced into a Google account.
- **Provider dependency (Google outage / policy change)** → *Mitigation:* magic link is an
  independent second path; users retain access if Google is unavailable. PAS owns its own
  session, not Google's.
- **Account-linking ambiguity (same email via Google and magic link)** → *Mitigation:* resolve
  identity by verified email; treat Google and magic-link sign-ins to the same verified email as
  the *same* identity — never create a duplicate. (Exact linking rule specified in PAS301D.)
- **Email deliverability for magic links (spam, delay, expiry)** → *Mitigation:* reputable
  transactional email, short single-use tokens, easy re-request, clear "check spam" guidance.
- **Phishing of magic links** → *Mitigation:* short expiry, single use, device/IP context
  hints, anti-replay; user education in copy.
- **OAuth scope creep / consent fatigue** → *Mitigation:* sign-in requests identity scope only;
  Gmail/Calendar/Drive scopes requested incrementally, in context, with explicit value — never
  bundled at the door.
- **Anti-enumeration** → *Mitigation:* never reveal whether an email has an account; uniform
  responses on sign-in/sign-up.
- **Enterprise pressure to add SSO early** → *Mitigation:* the model already leaves room
  (PAS301 §9); hold the line until a real enterprise deal requires it (PAS308 / enterprise
  path), rather than building it speculatively.

---

## 15. What not to implement yet

- **Email + password** at launch (revisit only if a real segment needs it).
- **Enterprise SSO / SAML** (deferred until an enterprise deal requires it).
- **Full Gmail/Calendar/Drive integration scopes** — auth chooses Google to *enable* these
  later; this decision does not build the integrations (PAS301 non-goals; PAS300 §21).
- **Device risk scoring, session-limit UI, advanced security** (PAS301 §25 "Later").
- **Any actual auth code, UI, backend, CORS, or packages** in this document.

This decision unblocks **PAS301D (Auth Provider Decision)** — it *is* the substance of that
decision — and clears the path for PAS301A/B shells and the later PAS301E/F implementation.

---

### Validation note

This document is **docs-only**. It makes **no** changes to code, UI, backend, CORS, auth
implementation, packages, the PAS209 work, or the parked stash. It records an authentication
strategy decision and the resulting UX direction; it implements none of it. Nothing is pushed.
