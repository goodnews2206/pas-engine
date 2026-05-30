/*
 * Demo communication layer — PAS Room + object threads + notifications.
 * Frontend-only. Communication is attached to operational work, not a
 * separate chat. Notification replies are local-only (demo-only).
 */

import {
  DEMO_META,
  type Notification,
  type NotificationReply,
  type ObjectThread,
} from "./types";

// ── Notifications ────────────────────────────────────────────────────────────

export const DEMO_NOTIFICATIONS: readonly Notification[] = [
  {
    ...DEMO_META,
    id: "NOTIF-0101",
    severity: "urgent",
    title: "Callback overdue",
    body: "CB-3301 was due at 2pm and has no recovery attempt logged.",
    module: "callbacks",
    ts: "2026-05-29T14:05:00Z",
    isRead: false,
    isDemoLabelled: true,
  },
  {
    ...DEMO_META,
    id: "NOTIF-0102",
    severity: "approval_required",
    title: "PAS proposes a bounded action",
    body: "Reassign CB-3301 to a covered agent. Approve to allow manual review.",
    module: "action-proposals",
    ts: "2026-05-29T14:06:00Z",
    isRead: false,
    isDemoLabelled: true,
  },
  {
    ...DEMO_META,
    id: "NOTIF-0103",
    severity: "needs_attention",
    title: "Three untouched Zillow leads",
    body: "Tuesday's leads still have no first contact.",
    module: "leads",
    ts: "2026-05-29T13:10:00Z",
    isRead: false,
    isDemoLabelled: true,
  },
  {
    ...DEMO_META,
    id: "NOTIF-0104",
    severity: "fyi",
    title: "Booking confirmed",
    body: "BK-4401 is on the calendar for Thursday.",
    module: "bookings",
    ts: "2026-05-29T09:25:00Z",
    isRead: true,
    isDemoLabelled: true,
  },
];

/**
 * Seed example of a captured local reply. Real replies are created
 * in-memory on submit (demo-only) and never reach a backend.
 */
export const DEMO_NOTIFICATION_REPLIES: readonly NotificationReply[] = [
  {
    ...DEMO_META,
    id: "REPLY-0101",
    notificationId: "NOTIF-0101",
    text: "Reassign this and have someone call before 3pm.",
    capturedAt: "2026-05-29T14:08:00Z",
  },
];

/** Confirmation copy shown after a local demo reply is captured. */
export const NOTIFICATION_REPLY_CONFIRMATION =
  "PAS captured this instruction in demo mode. No live action was taken.";

// ── PAS Room + object threads ────────────────────────────────────────────────

export const DEMO_THREADS: readonly ObjectThread[] = [
  {
    ...DEMO_META,
    id: "THREAD-room",
    objectType: "room",
    objectId: "northwind-demo",
    messages: [
      {
        ...DEMO_META,
        id: "MSG-0201",
        threadId: "THREAD-room",
        authorType: "pas",
        authorId: "PAS",
        type: "pas",
        body: "Callback CB-3301 is overdue. I've drafted a bounded recovery proposal.",
        evidenceIds: ["EV-8802"],
        ts: "2026-05-29T14:05:30Z",
      },
      {
        ...DEMO_META,
        id: "MSG-0202",
        threadId: "THREAD-room",
        authorType: "human",
        authorId: "U-OWNER-01",
        type: "human",
        body: "Good catch. Let's reassign to Riverside A.",
        evidenceIds: [],
        ts: "2026-05-29T14:07:00Z",
      },
      {
        ...DEMO_META,
        id: "MSG-0203",
        threadId: "THREAD-room",
        authorType: "human",
        authorId: "U-OWNER-01",
        type: "approval",
        body: "Approved for manual review: PROP-7701 (demo-only).",
        evidenceIds: ["EV-8802"],
        ts: "2026-05-29T14:08:00Z",
      },
    ],
  },
  {
    ...DEMO_META,
    id: "THREAD-callback-CB-3301",
    objectType: "callback",
    objectId: "CB-3301",
    messages: [
      {
        ...DEMO_META,
        id: "MSG-0211",
        threadId: "THREAD-callback-CB-3301",
        authorType: "human",
        authorId: "U-LEAD-01",
        type: "assignment",
        body: "Assigned CB-3301 to Riverside A (demo-only).",
        evidenceIds: [],
        ts: "2026-05-29T14:09:00Z",
      },
      {
        ...DEMO_META,
        id: "MSG-0212",
        threadId: "THREAD-callback-CB-3301",
        authorType: "pas",
        authorId: "PAS",
        type: "decision_record",
        body: "Recovery path recorded: reassign + call within the hour.",
        evidenceIds: ["EV-8802"],
        ts: "2026-05-29T14:09:30Z",
      },
    ],
  },
];
