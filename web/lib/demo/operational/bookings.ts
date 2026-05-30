/*
 * Demo bookings (Cal.com / Google Calendar style, simulated). Frontend-only.
 * Relations: sourceLeadId → leads, agentId → agents, evidenceIds → evidence.
 */

import { DEMO_META, type Booking } from "./types";

export const DEMO_BOOKINGS: readonly Booking[] = [
  {
    ...DEMO_META,
    id: "BK-4401",
    sourceLeadId: "D-1045",
    agentId: "AG-RIVERSIDE-01",
    status: "confirmed",
    evidenceIds: ["EV-8801"],
    calendarState: "On calendar — Thursday 10:00 (demo)",
    scheduledAt: "2026-06-04T14:00:00Z",
  },
  {
    ...DEMO_META,
    id: "BK-4402",
    sourceLeadId: "D-1042",
    agentId: "AG-RIVERSIDE-01",
    status: "requested",
    evidenceIds: [],
    calendarState: "Awaiting confirmation (demo)",
    scheduledAt: "2026-06-05T17:00:00Z",
  },
];
