/*
 * Demo action proposals — bounded, named, approval-gated. Frontend-only.
 * Approve/decline is demo-only; nothing executes. Mirrors the shape the
 * PAS209 backend will later feed (no wiring in this PR).
 * Relations: evidenceIds → evidence.
 */

import { DEMO_META, type ActionProposal } from "./types";

export const DEMO_PROPOSALS: readonly ActionProposal[] = [
  {
    ...DEMO_META,
    id: "PROP-7701",
    title: "Reassign overdue callback CB-3301 to a covered agent",
    scope: "Single callback · one named reassignment.",
    status: "candidate",
    expiresAt: "2026-05-29T18:00:00Z",
    evidenceIds: ["EV-8802"],
    actionPreview:
      "Would move CB-3301 from Riverside B to Riverside A and notify both. (demo-only)",
    auditLanguage:
      "PAS proposes one bounded action. No action is taken until a human approves. PAS has not changed live customer behavior.",
  },
  {
    ...DEMO_META,
    id: "PROP-7702",
    title: "Send first-touch template to three untouched Zillow leads",
    scope: "Three leads · one templated first-touch each.",
    status: "approved_for_manual_review",
    expiresAt: "2026-05-30T12:00:00Z",
    evidenceIds: ["EV-8804"],
    actionPreview:
      "Would queue a first-touch message for D-1043 and two peers for manual send. (demo-only)",
    auditLanguage:
      "Approved for manual review only. Nothing sends automatically. PAS has not changed live customer behavior.",
  },
];
