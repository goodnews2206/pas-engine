/*
 * Demo callbacks — the flagship "PAS watches commitments" object.
 * Frontend-only. Relations: leadId, ownerId, sourceCallId, evidence via calls.
 */

import { DEMO_META, type Callback } from "./types";

export const DEMO_CALLBACKS: readonly Callback[] = [
  {
    ...DEMO_META,
    id: "CB-3301",
    leadId: "D-1043",
    ownerId: "AG-RIVERSIDE-02",
    sourceCallId: "CALL-2211",
    promisedAt: "2026-05-29T13:05:00Z",
    dueAt: "2026-05-29T14:00:00Z",
    status: "overdue",
    riskLevel: "urgent",
    proposedRecovery:
      "Reassign to a covered agent and call within the hour. (demo-only)",
  },
  {
    ...DEMO_META,
    id: "CB-3302",
    leadId: "D-1042",
    ownerId: "AG-RIVERSIDE-01",
    sourceCallId: "CALL-2210",
    promisedAt: "2026-05-29T16:00:00Z",
    dueAt: "2026-05-30T16:00:00Z",
    status: "due_soon",
    riskLevel: "needs_attention",
    proposedRecovery: "Send a confirmation text before the due window. (demo-only)",
  },
  {
    ...DEMO_META,
    id: "CB-3303",
    leadId: "D-1044",
    ownerId: "AG-LAKESHORE-01",
    sourceCallId: "CALL-2212",
    promisedAt: "2026-05-28T18:45:00Z",
    dueAt: "2026-06-25T17:00:00Z",
    status: "promised",
    riskLevel: "fyi",
    proposedRecovery: "On track — nurture reminder set. (demo-only)",
  },
];
