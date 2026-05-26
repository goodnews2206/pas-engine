/*
 * Command Center demo data — frontend-only, build-time static.
 * No fetch, no API calls, no backend imports, no persistence.
 * Every export carries demoOnly: true and noLiveBehavior: true.
 * Authority: docs/pas_dashboard_information_architecture.md §4
 *            docs/pas_product_design_book.md §4.1
 */

export type AttentionSeverity =
  | "critical"
  | "urgent"
  | "approval-required"
  | "needs-attention";

export type SystemStatusKind =
  | "healthy"
  | "degraded"
  | "disconnected"
  | "demo";

export interface OperatingSummary {
  headline: string;
  context: string;
  attentionCount: number;
  proposalCount: number;
  demoOnly: true;
  noLiveBehavior: true;
}

export interface AttentionItem {
  id: string;
  severity: AttentionSeverity;
  title: string;
  body: string;
  actionLabel: string;
  actionHref: string;
  evidenceLabel: string;
  demoOnly: true;
  noLiveBehavior: true;
}

export interface RecommendationCard {
  id: string;
  title: string;
  scope: string;
  evidenceSummary: string;
  actionLabel: string;
  actionHref: string;
  expiresLabel: string;
  demoOnly: true;
  noLiveBehavior: true;
}

export interface PipelineRow {
  id: string;
  label: string;
  count: number;
  hint?: string;
  severityHint?: "attention" | "urgent";
  demoOnly: true;
  noLiveBehavior: true;
}

export interface SystemStatusItem {
  id: string;
  service: string;
  status: SystemStatusKind;
  detail: string;
  demoOnly: true;
  noLiveBehavior: true;
}

export interface EvidenceSignal {
  id: string;
  signal: string;
  source: string;
  demoOnly: true;
  noLiveBehavior: true;
}

// ── Operating summary ─────────────────────────────────────────────────────

export const OPERATING_SUMMARY: OperatingSummary = {
  headline:
    "PAS has found 3 items worth reviewing before the day gets away from the team.",
  context: "Demo snapshot · ORVN Demo Realty · Rehearsal only",
  attentionCount: 3,
  proposalCount: 2,
  demoOnly: true,
  noLiveBehavior: true,
};

// ── Needs attention (ordered critical → urgent → needs-attention) ──────────

export const ATTENTION_ITEMS: AttentionItem[] = [
  {
    id: "a-001",
    severity: "urgent",
    title: "Approval proposal expires in 28 minutes",
    body: "The re-engagement proposal for the Tuesday cohort will lapse at 14:56 UTC if not actioned. Sign off, decline, or it expires automatically.",
    actionLabel: "Review proposal",
    actionHref: "/action-proposals",
    evidenceLabel: "7 leads · avg 5.4 days idle",
    demoOnly: true,
    noLiveBehavior: true,
  },
  {
    id: "a-002",
    severity: "urgent",
    title: "5 promised callbacks not captured",
    body: "5 callbacks from the 10:00–12:00 call session have no system record. If not captured today, they will not appear in tomorrow's pipeline.",
    actionLabel: "Open callbacks",
    actionHref: "/callbacks",
    evidenceLabel: "10:00–12:00 session · 5 callbacks",
    demoOnly: true,
    noLiveBehavior: true,
  },
  {
    id: "a-003",
    severity: "needs-attention",
    title: "3 leads idle for 5 days",
    body: "3 leads from the Monday cohort have not been contacted since Monday. PAS drafted a re-engagement recommendation.",
    actionLabel: "View leads",
    actionHref: "/leads",
    evidenceLabel: "Monday cohort · 3 leads",
    demoOnly: true,
    noLiveBehavior: true,
  },
];

// ── PAS proposes ──────────────────────────────────────────────────────────

export const RECOMMENDATION_CARDS: RecommendationCard[] = [
  {
    id: "r-001",
    title: "Re-engage 7 stalled leads",
    scope: "Tuesday cohort",
    evidenceSummary:
      "7 leads, avg 5.4 days idle, 3 soft callbacks on record. PAS drafted a re-engagement sequence.",
    actionLabel: "Review proposal",
    actionHref: "/action-proposals",
    expiresLabel: "Expires today at 14:56 UTC",
    demoOnly: true,
    noLiveBehavior: true,
  },
  {
    id: "r-002",
    title: "Reassign 2 callbacks to Agent D",
    scope: "Callbacks · off-shift coverage",
    evidenceSummary:
      "Agent C is off-shift until tomorrow. 2 promised callbacks fall within the off-window. Agent D has capacity.",
    actionLabel: "Approve or decline",
    actionHref: "/action-proposals",
    expiresLabel: "Expires today at 18:00 UTC",
    demoOnly: true,
    noLiveBehavior: true,
  },
];

// ── Pipeline snapshot ─────────────────────────────────────────────────────

export const PIPELINE_ROWS: PipelineRow[] = [
  {
    id: "p-001",
    label: "Callbacks scheduled today",
    count: 7,
    demoOnly: true,
    noLiveBehavior: true,
  },
  {
    id: "p-002",
    label: "Bookings this week",
    count: 3,
    demoOnly: true,
    noLiveBehavior: true,
  },
  {
    id: "p-003",
    label: "Leads touched today",
    count: 11,
    demoOnly: true,
    noLiveBehavior: true,
  },
  {
    id: "p-004",
    label: "Open action proposals",
    count: 3,
    hint: "Awaiting review",
    severityHint: "attention",
    demoOnly: true,
    noLiveBehavior: true,
  },
  {
    id: "p-005",
    label: "Leads approaching stale",
    count: 4,
    hint: "No contact in 5+ days",
    severityHint: "attention",
    demoOnly: true,
    noLiveBehavior: true,
  },
];

// ── System status ─────────────────────────────────────────────────────────

export const SYSTEM_STATUS: SystemStatusItem[] = [
  {
    id: "s-001",
    service: "PAS API",
    status: "healthy",
    detail: "Responding normally",
    demoOnly: true,
    noLiveBehavior: true,
  },
  {
    id: "s-002",
    service: "Twilio",
    status: "degraded",
    detail: "3 inbound calls dropped — check call routing",
    demoOnly: true,
    noLiveBehavior: true,
  },
  {
    id: "s-003",
    service: "Cal.com",
    status: "disconnected",
    detail: "Auth token expired at 14:02 UTC — bookings failing",
    demoOnly: true,
    noLiveBehavior: true,
  },
  {
    id: "s-004",
    service: "Supabase",
    status: "healthy",
    detail: "Connected",
    demoOnly: true,
    noLiveBehavior: true,
  },
  {
    id: "s-005",
    service: "Demo mode",
    status: "demo",
    detail: "No live customer behavior",
    demoOnly: true,
    noLiveBehavior: true,
  },
];

// ── Rehearsal evidence ────────────────────────────────────────────────────

export const EVIDENCE_SIGNALS: EvidenceSignal[] = [
  {
    id: "e-001",
    signal:
      "PAS Brain learned \"we'd love a quick chat\" as a soft callback signal",
    source: "4 calls this week — rehearsal dataset",
    demoOnly: true,
    noLiveBehavior: true,
  },
  {
    id: "e-002",
    signal:
      "Tuesday cohort shows below-average contact rate across 5 days",
    source: "7-day pipeline simulation — demo only",
    demoOnly: true,
    noLiveBehavior: true,
  },
  {
    id: "e-003",
    signal:
      "Rehearsal call sentiment average 0.31 — neutral-low for this cohort",
    source: "Demo call dataset — not from live calls",
    demoOnly: true,
    noLiveBehavior: true,
  },
];
