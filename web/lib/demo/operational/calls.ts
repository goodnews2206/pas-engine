/*
 * Demo call records. Frontend-only. Transcript previews are fictional.
 * Relations: leadId → leads, agentId → agents, evidenceIds → evidence.
 */

import { DEMO_META, type Call } from "./types";

export const DEMO_CALLS: readonly Call[] = [
  {
    ...DEMO_META,
    id: "CALL-2210",
    leadId: "D-1042",
    agentId: "AG-RIVERSIDE-01",
    outcome: "connected",
    transcriptPreview:
      "“…if the right place came up, how soon could you move?” (simulated transcript)",
    objection: "Wants to see closing timeline before committing.",
    sentiment: "positive",
    evidenceIds: ["EV-8801"],
    nextAction: "Schedule a showing this week.",
    occurredAt: "2026-05-29T15:55:00Z",
  },
  {
    ...DEMO_META,
    id: "CALL-2211",
    leadId: "D-1043",
    agentId: "AG-RIVERSIDE-02",
    outcome: "voicemail",
    transcriptPreview: "Left a voicemail; no callback logged. (simulated)",
    objection: "n/a",
    sentiment: "neutral",
    evidenceIds: ["EV-8802"],
    nextAction: "Retry call and log the attempt.",
    occurredAt: "2026-05-29T13:00:00Z",
  },
  {
    ...DEMO_META,
    id: "CALL-2212",
    leadId: "D-1044",
    agentId: "AG-LAKESHORE-01",
    outcome: "scheduled_callback",
    transcriptPreview:
      "Buyer asked to be contacted next month after a relocation. (simulated)",
    objection: "Timing — relocating in ~6 months.",
    sentiment: "hesitant",
    evidenceIds: [],
    nextAction: "Set a nurture reminder.",
    occurredAt: "2026-05-28T18:40:00Z",
  },
];
