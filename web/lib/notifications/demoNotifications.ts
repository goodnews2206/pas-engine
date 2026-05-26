/*
 * PAS demo notification dataset — frontend-only, build-time static data.
 * No fetch, no API calls, no persistence, no backend imports.
 * Authority: docs/pas_notification_architecture.md §2 (severity model) §7 (copy rules).
 */

export type SeverityLevel =
  | "fyi"
  | "needs-attention"
  | "urgent"
  | "approval-required"
  | "critical";

export interface DemoNotification {
  id: string;
  severity: SeverityLevel;
  title: string;
  body: string;
  module: string;
  moduleHref: string;
  timestamp: string;
  relativeTime: string;
  isRead: boolean;
  isDemoLabelled: boolean;
  actionLabel?: string;
  actionHref?: string;
}

export const DEMO_NOTIFICATIONS: DemoNotification[] = [
  // ── Critical ──────────────────────────────────────────────────────────
  {
    id: "n-001",
    severity: "critical",
    title: "Cal.com auth token expired — bookings failing",
    body: "New booking attempts have returned 401 since 14:02 UTC. Prospects cannot complete booking. Reconnect from Integrations.",
    module: "Integrations",
    moduleHref: "/integrations",
    timestamp: "2026-05-26T14:02:00Z",
    relativeTime: "47 min ago",
    isRead: false,
    isDemoLabelled: true,
    actionLabel: "Open Integrations",
    actionHref: "/integrations",
  },
  {
    id: "n-002",
    severity: "critical",
    title: "Twilio call routing failed — 3 inbound calls dropped",
    body: "PAS detected 3 unanswered inbound calls in the last 90 minutes with no fallback routing active. Leads may have been missed.",
    module: "Calls",
    moduleHref: "/calls",
    timestamp: "2026-05-26T13:28:00Z",
    relativeTime: "1 hr 21 min ago",
    isRead: false,
    isDemoLabelled: true,
    actionLabel: "Review calls",
    actionHref: "/calls",
  },

  // ── Approval required ─────────────────────────────────────────────────
  {
    id: "n-003",
    severity: "approval-required",
    title: "PAS proposes re-engaging 7 stalled leads",
    body: "7 leads from the Tuesday cohort have not been contacted in 5 days. PAS drafted a re-engagement sequence based on call sentiment signals. Evidence: avg 5.4 days idle, 3 prior soft callbacks noted.",
    module: "Action Proposals",
    moduleHref: "/action-proposals",
    timestamp: "2026-05-26T11:00:00Z",
    relativeTime: "3 hr 49 min ago",
    isRead: false,
    isDemoLabelled: true,
    actionLabel: "Review proposal",
    actionHref: "/action-proposals",
  },
  {
    id: "n-004",
    severity: "approval-required",
    title: "PAS proposes reassigning 2 callbacks",
    body: "Agent C is off-shift until tomorrow. 2 promised callbacks fall within the off-window. PAS would like to reassign them to Agent D who has capacity.",
    module: "Action Proposals",
    moduleHref: "/action-proposals",
    timestamp: "2026-05-26T10:15:00Z",
    relativeTime: "4 hr 34 min ago",
    isRead: false,
    isDemoLabelled: true,
    actionLabel: "Approve or decline",
    actionHref: "/action-proposals",
  },
  {
    id: "n-005",
    severity: "approval-required",
    title: "PAS proposes moving 3 leads to Nurture",
    body: "Call sentiment analysis indicates 3 leads in the 'New' stage are unlikely to convert without a nurture sequence. PAS drafted the stage transition. Evidence: 2 calls per lead, avg sentiment score 0.31.",
    module: "Action Proposals",
    moduleHref: "/action-proposals",
    timestamp: "2026-05-26T09:30:00Z",
    relativeTime: "5 hr 19 min ago",
    isRead: true,
    isDemoLabelled: true,
    actionLabel: "Review evidence",
    actionHref: "/action-proposals",
  },

  // ── Urgent ────────────────────────────────────────────────────────────
  {
    id: "n-006",
    severity: "urgent",
    title: "Approval proposal expires in 28 minutes",
    body: "The re-engagement proposal for the Tuesday cohort will lapse with no action at 14:56 UTC. Sign off, decline, or it expires automatically.",
    module: "Action Proposals",
    moduleHref: "/action-proposals",
    timestamp: "2026-05-26T14:28:00Z",
    relativeTime: "21 min ago",
    isRead: false,
    isDemoLabelled: true,
    actionLabel: "Go to proposal",
    actionHref: "/action-proposals",
  },
  {
    id: "n-007",
    severity: "urgent",
    title: "5 promised callbacks not captured",
    body: "5 callbacks were promised in the 10:00–12:00 call session. None have been logged in the system. If not captured today, they will not appear in tomorrow's pipeline.",
    module: "Callbacks",
    moduleHref: "/callbacks",
    timestamp: "2026-05-26T12:30:00Z",
    relativeTime: "2 hr 19 min ago",
    isRead: false,
    isDemoLabelled: true,
    actionLabel: "Open callbacks",
    actionHref: "/callbacks",
  },
  {
    id: "n-008",
    severity: "urgent",
    title: "High-value lead idle for 72 hours",
    body: "Lead J. Morrison has not been contacted in 72 hours and is approaching the stale threshold. PAS notes 2 prior inbound calls and a soft tour request signal.",
    module: "Leads",
    moduleHref: "/leads",
    timestamp: "2026-05-26T10:45:00Z",
    relativeTime: "4 hr 4 min ago",
    isRead: true,
    isDemoLabelled: true,
    actionLabel: "View lead",
    actionHref: "/leads",
  },

  // ── Needs attention ───────────────────────────────────────────────────
  {
    id: "n-009",
    severity: "needs-attention",
    title: "3 leads idle for 5 days — re-engagement ready",
    body: "3 leads from the Monday cohort have not been touched in 5 days. A re-engagement recommendation is drafted and visible in Command Center.",
    module: "Leads",
    moduleHref: "/leads",
    timestamp: "2026-05-26T08:00:00Z",
    relativeTime: "6 hr 49 min ago",
    isRead: false,
    isDemoLabelled: true,
    actionLabel: "View leads",
    actionHref: "/leads",
  },
  {
    id: "n-010",
    severity: "needs-attention",
    title: "Simulation projects 14% conversion drop",
    body: "Pipeline simulation projects a 14% drop in conversion rate if current call volume is sustained for another 7 days. Based on 30-day historical patterns.",
    module: "Pipeline Risks",
    moduleHref: "/pipeline-risks",
    timestamp: "2026-05-26T07:30:00Z",
    relativeTime: "7 hr 19 min ago",
    isRead: false,
    isDemoLabelled: true,
    actionLabel: "Review risks",
    actionHref: "/pipeline-risks",
  },
  {
    id: "n-011",
    severity: "needs-attention",
    title: "6 tour-requested leads overdue for follow-up",
    body: "6 leads in the 'tour requested' cohort are past the recommended follow-up window. PAS drafted a recommendation with a prioritised contact order.",
    module: "Recommendations",
    moduleHref: "/recommendations",
    timestamp: "2026-05-25T16:00:00Z",
    relativeTime: "22 hr ago",
    isRead: true,
    isDemoLabelled: true,
    actionLabel: "View recommendation",
    actionHref: "/recommendations",
  },
  {
    id: "n-012",
    severity: "needs-attention",
    title: "Daily call quota at 82% with 3 hours remaining",
    body: "Call volume is tracking below target. 82% of the daily quota is complete with 3 hours left in the business day. No automated action will be taken.",
    module: "Calls",
    moduleHref: "/calls",
    timestamp: "2026-05-26T12:00:00Z",
    relativeTime: "2 hr 49 min ago",
    isRead: true,
    isDemoLabelled: true,
  },

  // ── FYI ──────────────────────────────────────────────────────────────
  {
    id: "n-013",
    severity: "fyi",
    title: "PAS Brain learned a new soft callback signal",
    body: "\"We'd love a quick chat\" was identified as a soft callback request across 4 calls this week. No action needed — PAS will apply this to future intent scoring.",
    module: "Evidence Digest",
    moduleHref: "/evidence-digest",
    timestamp: "2026-05-26T09:00:00Z",
    relativeTime: "5 hr 49 min ago",
    isRead: true,
    isDemoLabelled: true,
  },
  {
    id: "n-014",
    severity: "fyi",
    title: "Daily call volume within normal range",
    body: "Call volume for today is within the expected range based on historical patterns. No operational changes suggested.",
    module: "Evidence Digest",
    moduleHref: "/evidence-digest",
    timestamp: "2026-05-26T08:30:00Z",
    relativeTime: "6 hr 19 min ago",
    isRead: true,
    isDemoLabelled: true,
  },
  {
    id: "n-015",
    severity: "fyi",
    title: "Simulation Lab overnight scenario run complete",
    body: "The scheduled scenario run completed at 03:14 UTC. Results are available in Simulation Lab. No anomalies detected in the overnight run.",
    module: "Simulation Lab",
    moduleHref: "/simulation-lab",
    timestamp: "2026-05-26T03:14:00Z",
    relativeTime: "11 hr 35 min ago",
    isRead: true,
    isDemoLabelled: true,
  },
];
