# Demo Environment Checklist

**Run this before every demo.** A failed live demo costs you the deal and your credibility. The rule: **never demo live without a tested fallback ready to go.** Everything below assumes PAS stays read-only — no mutations, no outbound, nothing changed for the demo.

---

## 1. Pre-demo checks (T-minus 30 min)

- [ ] Know the audience: brokerage name, # agents, lead sources, the one pain you'll anchor on.
- [ ] Decide demo mode: **live tenant data** (if a design partner with the snapshot bridge enabled) or **demo/seeded data**. Know which, and be ready to say the source out loud.
- [ ] App/server reachable and responding to a health check.
- [ ] Network: tested connection + a phone hotspot as backup.
- [ ] Browser tabs pre-opened and logged in: operational view, Slack workspace, calendar.
- [ ] Recorded backup ready (see §7) in case anything live fails.
- [ ] Silence notifications; close anything with other clients' data visible (tenant hygiene).
- [ ] Have the [Founder Demo Script](pas210_1_founder_demo_script.md) open on a second screen.

---

## 2. Voice-flow checks

- [ ] Inbound demo number answers on the first ring.
- [ ] Greeting plays cleanly; audio is clear both directions.
- [ ] Qualification flow captures intent → budget → timeline correctly on a test call.
- [ ] An objection ("I'm just looking") is handled gracefully, not dropped.
- [ ] The call produces a clean structured record at the end.
- [ ] If using a real number, confirm it's pointed at the demo environment, not a client's production line.

---

## 3. Booking checks

- [ ] Calendar is connected and shows test availability.
- [ ] The booking branch creates a visible appointment on the test calendar.
- [ ] The callback branch captures a requested time + best number and confirms before hangup.
- [ ] Confirmation/notification path (if shown) points to a test inbox/number, not a real client.
- [ ] No real lead data is exposed in any booking screen you'll share.

---

## 4. Observer checks (the emotional peak — do not skip)

- [ ] The "what needs attention" / operational digest renders without errors.
- [ ] It shows believable signals: leads waiting, callbacks due, unassigned high-value lead, failed calls.
- [ ] **Source transparency:** the result clearly indicates demo vs. live. If live, confirm it's the **correct tenant** and say so.
- [ ] If using the live snapshot bridge: flag is set correctly, `brokerage_id` resolves, and it does **not** silently fall back — you see live data or an explicit "unavailable," never a silent blend.
- [ ] The "calls today" / "hot leads" style reads are populated and sane.

---

## 5. Slack checks

- [ ] PAS responds in the demo Slack workspace.
- [ ] `what needs attention` returns the digest.
- [ ] `calls today`, `hot leads`, `stats` return clean, PII-safe output.
- [ ] Responses render readably in Slack (no raw payloads, no errors).
- [ ] You're in the **demo** workspace, not a partner's real one.

---

## 6. Tenant & safety hygiene (every time)

- [ ] Only the intended brokerage's data is visible anywhere on screen.
- [ ] No secrets, API keys, or raw PII shown in any surface you share.
- [ ] PAS performs no mutations and takes no outbound action during the demo (it can't, but verify nothing is misconfigured).

---

## 7. Backup plan if live systems fail

**Have these ready before you start — assume something will break.**

1. **Recorded walkthrough:** a 3–5 min screen recording of the full happy path (call → qualify → book/callback → observer → Slack). If anything live breaks, switch to it without apology: *"Let me show you the clean version of this flow."*
2. **Seeded demo data:** if live tenant data is unavailable, fall back to the deterministic demo snapshot — and **say so**: *"This is sample data so you can see the shape; we'll run it on your real numbers in the pilot."* Never present demo data as live.
3. **Screenshots deck:** static images of each surface as a last resort if there's no connectivity at all.
4. **Pivot to the audit:** if the tech is fully down, run the [Lead Continuity Audit](pas210_1_lead_continuity_audit.md) instead — it needs nothing but a conversation and closes just as well.

**Golden rule:** if you can't show it cleanly and honestly, don't show it — talk about *their* leakage instead. A confident diagnostic beats a broken demo every time.

---

## Post-demo (T-plus 5 min)
- [ ] Confirmed next step on the calendar (audit or design-partner discussion).
- [ ] Captured their reactions/objections verbatim for follow-up.
- [ ] Reset/clear any demo state if a real number or calendar was used.

→ Related: [Founder Demo Script](pas210_1_founder_demo_script.md) · [Discovery Framework](pas210_1_discovery_framework.md) · [Objection Handling](pas210_1_objection_handling.md)
