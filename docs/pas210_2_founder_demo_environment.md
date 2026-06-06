# PAS210.2 — Founder Demo Environment

**Type:** Demoability specification — documentation only. No runtime code, tests, migrations, or product capabilities are added here. This defines *how* PAS is demonstrated deterministically; implementation of any seed is a separate, later task.

**Objective:** A brokerage owner understands PAS in < 5 minutes, and the founder can run the demo reliably **without waiting on live inbound traffic, live lead arrivals, or production timing.**

**Doctrine (unchanged):** PAS makes a company *queryable, adaptive, and operationally intelligent.* PAS remains read-only and observational.

---

## Task 1 — Current demoability audit

What exists today, by surface:

| Surface | Backing | Needs live traffic? | Deterministic? |
|---|---|---|---|
| **Text qualification** | `/simulate-call` ([app/routes/simulate.py](../app/routes/simulate.py)) runs the **real** `PASEngine` — no Twilio/Deepgram/ElevenLabs | No | Yes, **if** the founder types the same script |
| **Voice qualification** | `/demo/token` ([app/routes/demo.py](../app/routes/demo.py)) browser call via Twilio | Yes (a placed call) | Returns **503** unless `TWILIO_API_KEY_SID`/`API_SECRET`/`TWIML_APP_SID` set |
| **Booking** | state machine BOOKING branch → `calcom_client` | No (within a sim call) | Real if Cal.com key set; otherwise **labelled simulated** booking |
| **Callback capture** | state machine PAS128 callback sub-flow | No | Yes |
| **Observer / risk (flag OFF)** | `build_demo_snapshot()` ([proactive_digest_intent.py:214](../app/services/slack/proactive_digest_intent.py)) — deterministic in-memory snapshot | No | **Yes, fully** |
| **Observer / risk (flag ON / live)** | PAS210 bridge → PAS206 adapter → Supabase, per-tenant | Yes (needs rows in DB) | Only as deterministic as the seeded DB |
| **Slack surface** | intents render the same snapshot/queries | No (for render) | Yes, but needs a Slack workspace + signing secret configured |

**Can a founder reliably demonstrate the six beats without live events?**

| Beat | Reliable today? | Path |
|---|---|---|
| 1. Lead enters | ✅ (text) / ⚠️ (voice) | `/simulate-call` always works; voice needs Twilio creds |
| 2. PAS responds | ✅ | real `PASEngine` greeting |
| 3. PAS qualifies | ✅ | intent → budget → timeline captured |
| 4. PAS books | ✅ (⚠️ label) | books on Cal.com, or a clearly-labelled simulated booking |
| 5. PAS observes | ✅ (flag OFF) / ⚠️ (live) | demo snapshot is rich; **live demo brokerage is empty** |
| 6. PAS identifies risk | ✅ (flag OFF) / ⚠️ (live) | snapshot encodes the risk signals; live needs seeded rows |

**Documented gaps:**
- **G1 — Live observer is empty.** [seed_demo_brokerage.sql](../scripts/seed_demo_brokerage.sql) seeds **only the brokerage row** (0 leads/calls/bookings/callbacks/agents). The compelling observer narrative exists only in the **in-memory** `build_demo_snapshot` (flag OFF). A flag-ON live demo against `demo` shows nothing.
- **G2 — Two disconnected demo worlds.** Flag-OFF narrative (in-memory snapshot) ≠ flag-ON narrative (empty DB). They tell different stories.
- **G3 — Voice demo is config-dependent.** `/demo/token` 503s without Twilio API-key creds; live voice can't be guaranteed on the road.
- **G4 — Booking realism varies.** Without a Cal.com key the booking is simulated (correctly labelled, but the founder must narrate it).
- **G5 — Text determinism is operator-dependent.** `/simulate-call` is only as repeatable as the founder's typed inputs; there's no canned script.
- **G6 — Seed fragmentation.** Two seed artifacts exist — `seed_demo_brokerage.sql` (brokerage only) and [wf_seed_demo_call.py](../scripts/wf_seed_demo_call.py) (the single README call `SIM-YC-W26-CALLBACK-001`) — and neither produces a full operational pipeline.
- **G7 — No reset runbook.** No documented "return the demo to a known state" procedure.

---

## Task 2 — Demo story audit (PAS210.1 script → runnable functionality)

Mapping each beat of the [Founder Demo Script](pas210_1_founder_demo_script.md):

| Script beat | Status | Backing / note |
|---|---|---|
| Beat 1 — First contact (call answered) | **Supported** (text) / **Partially supported** (voice) | `/simulate-call` always; voice needs Twilio creds (G3) |
| Beat 2 — Qualification in their words | **Supported** | real state machine, intent/budget/timeline |
| Beat 3a — Booking on calendar | **Supported / Simulated** | Cal.com if keyed, else labelled simulated booking (G4) |
| Beat 3b — Callback captured | **Supported** | PAS128 callback sub-flow |
| Beat 4 — "What needs attention" (observe) | **Supported (flag OFF)** / **Simulated** | rich in-memory snapshot; live path empty (G1/G2) |
| Beat 4 — live, "your numbers not a sample" | **Missing** (today) | requires seeded operational rows in the demo brokerage |
| Beat 5 — Ask it in Slack | **Supported** (render) / **Partially** (setup) | needs Slack workspace + signing secret configured |
| Source transparency (demo vs live) | **Supported** | PAS210 `source_mode` ∈ {demo, live, unavailable} |

**Summary:** every beat is demonstrable **today via the text + flag-OFF path**. The only **missing** capability is a *live* observer demo on the demo brokerage — closed by seeding (Task 4), not by new product code.

---

## Task 3 — Demo environment specification

Goal: **every demo run produces the same narrative.** The canonical demo tenant is `demo` ("ORVN Realty", agent "Alex"). Below is the target state the environment should hold (to be implemented by a seed; specified here only).

### A. Demo brokerage
- `id="demo"`, `name="ORVN Realty"`, `agent_name="Alex"`, `active=true`. (Exists today.)
- Flag posture documented per demo: `PAS_LIVE_OPERATIONAL_SNAPSHOT_ENABLED` **off** for the zero-dependency narrative; **on** only when the operational seed is present.

### B. Demo agents
- `A-1` "Jordan" — available, standard specialties.
- `A-2` "Sam" — busy/unavailable (drives the "no agent available" signal).

### C. Demo leads
- `L-901` — high-value, source `web`, **unassigned**, no first response (drives "high-value waiting" + "missed first response").
- `L-902` — standard, source `referral`, assigned `A-1`, `needs_human_review=true`.
- `L-903` — standard, recent, healthy (a clean lead so the digest isn't all red).

### D. Demo calls
- Three calls on `L-901` (`C-701/702/703`), outcome `failed` (drives "repeated failed calls").
- One completed, booked call on `L-903` (the happy path).
- `SIM-YC-W26-CALLBACK-001` — the README workflow call (callback narrative), already seedable via `wf_seed_demo_call.py`.

### E. Demo bookings
- `B-501` on `L-903` — confirmed (happy path on the calendar).
- `B-502` on `L-902` — **failed confirmation** (drives "failed booking confirmation").

### F. Demo callbacks
- One **overdue** callback on `L-901` (drives "callback overdue").
- One on-time callback on `L-903` (contrast).

### G. Demo operational risks (the signals the observer should surface)
Deterministically, the digest should show: high-value lead waiting, missed first response, repeated failed calls (L-901); needs-human-review (L-902); failed booking confirmation (B-502); callback overdue; no agent available (A-2). This mirrors the existing `build_demo_snapshot` so flag-OFF and flag-ON tell the **same** story.

### H. Demo Slack outputs
- `what needs attention` → the digest enumerating G's signals, PII-free, with `source_mode` shown.
- `calls today` → counts reflecting D.
- `hot leads` → L-901 surfaced.
- `stats` → labelled "demo" when `demo_data_detector` flags the tenant.

---

## Task 4 — Demo data strategy

Options and trade-offs:

| Strategy | Pros | Cons | Verdict |
|---|---|---|---|
| **Seeded** (durable, idempotent SQL/Python writing fixed rows to the demo brokerage) | Deterministic; durable; exercises the **real** DB → PAS206 → observer path; same on every run; survives restarts | Must be maintained as schema evolves; one-time write to set up | ✅ **Recommend (live path)** |
| **Synthetic in-memory** (today's `build_demo_snapshot`) | Zero dependencies; perfect determinism; already exists | Bypasses DB and the live path — proves the renderer, not the bridge | ✅ **Keep (flag-OFF path)** |
| **Generated** (procedural/random) | Fresh-looking data | Non-deterministic → breaks "same narrative every time" | ❌ Reject |
| **Replayed** (record real calls, replay events) | Most realistic | Needs production traffic PAS doesn't have; PAS141 replay is retired/bytecode-only; heavy harness | ❌ Not now |

**Recommendation: a hybrid that is "seeded for live, synthetic for offline."**
- Keep `build_demo_snapshot` as the **zero-dependency, flag-OFF** demo (always works on the road).
- Implement a single **idempotent seed** that writes the Task 3 (B–F) rows into the `demo` brokerage so the **flag-ON live** demo reproduces the identical narrative on the real PAS206 path. Unify `seed_demo_brokerage.sql` + `wf_seed_demo_call.py` into one repeatable operational seed + a reset step.
- **Do not implement here** — this is the spec; the seed is the next small sales-enablement task (see Task 8).

---

## Task 5 — Demo flow specification

Each run maps to real PAS functionality.

### Demo Run A — Lead continuity failure *(observe)*
- **Surface:** observer digest (flag OFF) or Slack `what needs attention`.
- **Narrative:** L-901 — high-value web lead, unassigned, three failed calls, no first response.
- **Signals shown:** high-value waiting + missed first response + repeated failed calls.
- **Line:** "This is a paid lead actively slipping — and nobody could see it until now."

### Demo Run B — Successful qualification *(answer → qualify → book)*
- **Surface:** `/simulate-call` (text), buyer script.
- **Flow:** greeting → intent (buy) → budget → timeline → booking consent → booking confirmed (Cal.com or labelled simulated) → clean structured record.
- **Line:** "Every answer captured, a viewing on the calendar, the agent starts from a qualified lead."

### Demo Run C — Missed callback *(capture + observe)*
- **Surface:** `/simulate-call` where the lead asks for a callback (captured: time + best number) **then** the observer shows the overdue callback on L-901.
- **Line:** "PAS captured the promise — and would have shown you the moment it was at risk of being broken."

### Demo Run D — Operational risk detection *(query)*
- **Surface:** Slack `what needs attention` (or the observer digest).
- **Flow:** the digest enumerates the full Task 3-G signal set with `source_mode` visible.
- **Line:** "Your pipeline, queryable, in plain English — read-only eyes on the whole operation."

---

## Task 6 — Design partner demo checklist (founder pre-flight)

Verify before any live broker demo (complements [demo checklist](pas210_1_demo_checklist.md)):

- [ ] **Decide path:** text-sim + flag-OFF (always reliable) vs. live voice/observer (needs config + seed).
- [ ] **Twilio ready** (only if doing voice): `TWILIO_API_KEY_SID` / `TWILIO_API_SECRET` / `TWILIO_TWIML_APP_SID` set; `/demo/token` returns a token, not 503.
- [ ] **Booking ready:** Cal.com keyed (real booking) **or** founder ready to narrate the labelled simulated booking.
- [ ] **Slack ready:** demo workspace linked, signing secret set; `what needs attention` / `calls today` / `hot leads` / `stats` return clean output.
- [ ] **Demo records present:** demo brokerage seeded; operational rows (Task 3 B–F) present if running **live**; `wf_seed_demo_call.py` run so `SIM-YC-W26-CALLBACK-001` resolves.
- [ ] **Observer functioning:** digest renders without error and shows the expected signal set.
- [ ] **PAS210 source mode visible:** flag state known; result shows `source_mode` (demo/live/unavailable); **no silent fallback** observed.
- [ ] **Tenant hygiene:** only `demo`/the partner tenant visible; no other client data, no secrets/PII on screen.
- [ ] **Backup ready:** recorded walkthrough + screenshots, per PAS210.1 §7.

---

## Task 7 — First customer readiness assessment

**Technical gaps**
- T1 — Live demo brokerage has **no seeded operational rows** → flag-ON observer empty (G1/G2). *Closed by the seed (Task 4).*
- T2 — Voice demo depends on Twilio API-key config (G3).
- T3 — Booking realism depends on Cal.com key, else labelled-simulated (G4).
- T4 — Slack demo requires workspace + signing secret configured.
- T5 — Seed fragmentation; no unified, idempotent operational seed (G6).

**Operational gaps**
- O1 — No "reset demo to known state" runbook (G7).
- O2 — Text-sim determinism depends on the founder typing a consistent script (G5) → needs a canned script card.
- O3 — No documented canonical demo phone number / Slack workspace / calendar for the road.

**Sales gaps**
- S1 — Largely closed by PAS210.1 (script, audit, discovery, objections, program, checklist).
- S2 — Remaining: founder rehearsal reps and a tightened 5-minute path; this spec supplies the deterministic flows to rehearse against.

**Bottom line:** PAS can be demonstrated effectively **today** via the text + flag-OFF observer path. The only thing standing between that and a *live* "your-own-numbers" demo is a small, deterministic **seed** — not product engineering.

---

## Task 8 — PAS211 readiness

**Does PAS211 (Minimal Runtime Security Recovery) remain the correct next *engineering* checkpoint? Yes.**

- The PAS209.6 sequence holds: runtime/security before growth. PAS211 rebuilds the real hardening (api-key rotation/reveal, HTTPS enforcement, operator auth, CORS/redirect guards) that a paying brokerage's data warrants — it should precede memory (PAS212) and ingestion (PAS213).
- PAS210.2 did **not** add product capability; it surfaced a **sales-enablement** task (the demo seed), which is not an engineering checkpoint and does not displace PAS211 in the build order.

**Recommendation:** keep **PAS211** as the next engineering checkpoint. If a *live-mode* demo is needed inside the 14-day window, slot a tiny **PAS210.3 — Demo Operational Seed** (implement the Task 3/Task 4 idempotent seed + reset runbook) as a parallel sales-enablement task — small, isolated, read-only-friendly, and explicitly **not** a product expansion. Engineering trunk proceeds to PAS211 regardless.

---

*End of PAS210.2 — founder demo environment specification. Documentation only; no runtime code, tests, or migrations changed. PAS209 untouched, parked stash untouched, no `__pycache__` deleted, no dependencies added.*
