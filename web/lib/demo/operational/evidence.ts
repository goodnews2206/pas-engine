/*
 * Demo evidence signals — the "receipts" PAS links to. Frontend-only.
 * Referenced by calls, callbacks, bookings, risks, recommendations,
 * and proposals via evidenceIds.
 */

import { DEMO_META, type EvidenceSignal } from "./types";

export const DEMO_EVIDENCE: readonly EvidenceSignal[] = [
  {
    ...DEMO_META,
    id: "EV-8801",
    kind: "call_transcript",
    source: "call",
    summary:
      "Simulated call CALL-2210: lead asked about closing timeline twice — buying intent signal.",
    link: "/calls?inspect=CALL-2210",
  },
  {
    ...DEMO_META,
    id: "EV-8802",
    kind: "missed_commitment",
    source: "signal",
    summary:
      "Simulated: callback CB-3301 promised for 2pm was not logged as completed.",
    link: "/callbacks?inspect=CB-3301",
  },
  {
    ...DEMO_META,
    id: "EV-8803",
    kind: "response_latency",
    source: "signal",
    summary:
      "Simulated: Riverside B first-response time trended above the 10-minute target this week.",
    link: "/agents?inspect=AG-RIVERSIDE-02",
  },
  {
    ...DEMO_META,
    id: "EV-8804",
    kind: "recommendation_basis",
    source: "recommendation",
    summary:
      "Simulated: three Zillow leads from Tuesday remain in 'new' with no first touch.",
    link: "/recommendations?inspect=REC-6601",
  },
];
