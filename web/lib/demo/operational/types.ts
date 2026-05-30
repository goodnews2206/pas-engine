/*
 * PAS operational demo data model — types + closed vocabularies.
 *
 * Frontend-only. No backend, no API, no network, no mutations, no auth.
 * Every exported demo object carries `demoOnly: true` + `noLiveBehavior: true`.
 * This is the single source of demo truth consumed by later module PRs
 * (see docs/pas_operational_demo_layer_plan.md §7 and §10).
 *
 * Nothing here implies real clients. All data is clearly fictional.
 */

// ─────────────────────────────────────────────────────────────────────────────
// Demo safety meta — stamped on every object
// ─────────────────────────────────────────────────────────────────────────────

export interface DemoMeta {
  readonly demoOnly: true;
  readonly noLiveBehavior: true;
}

/** Spread into every demo object to guarantee the safety invariant. */
export const DEMO_META = {
  demoOnly: true,
  noLiveBehavior: true,
} as const satisfies DemoMeta;

// ─────────────────────────────────────────────────────────────────────────────
// Relation IDs (string aliases — documented shapes, not branded types)
// ─────────────────────────────────────────────────────────────────────────────

export type AgentId = string; // e.g. "AG-RIVERSIDE-01"
export type UserId = string; // e.g. "U-OWNER-01"
export type LeadId = string; // e.g. "D-1042"
export type CallId = string; // e.g. "CALL-2210"
export type CallbackId = string; // e.g. "CB-3301"
export type BookingId = string; // e.g. "BK-4401"
export type RiskId = string; // e.g. "RISK-5501"
export type RecommendationId = string; // e.g. "REC-6601"
export type ProposalId = string; // e.g. "PROP-7701"
export type EvidenceId = string; // e.g. "EV-8801"
export type IntegrationId = string; // e.g. "INT-followupboss"
export type MemoryId = string; // e.g. "MEM-9901"
export type NotificationId = string; // e.g. "NOTIF-0101"
export type ReplyId = string; // e.g. "REPLY-0101"
export type MessageId = string; // e.g. "MSG-0201"
export type ThreadId = string; // e.g. "THREAD-lead-D-1042"

/** ISO-8601 timestamp string (fixed demo literals; no runtime clock). */
export type IsoTimestamp = string;

// ─────────────────────────────────────────────────────────────────────────────
// Closed vocabularies
// ─────────────────────────────────────────────────────────────────────────────

export type Severity =
  | "fyi"
  | "needs_attention"
  | "urgent"
  | "approval_required"
  | "critical";

export type IntegrationStatus =
  | "not_connected"
  | "connected_read_only"
  | "write_approval_required"
  | "degraded";

export type ProposalStatus =
  | "candidate"
  | "approved_for_manual_review"
  | "rejected"
  | "deferred";

export type LeadStage =
  | "new"
  | "contacted"
  | "qualified"
  | "nurturing"
  | "appointment_set"
  | "won"
  | "lost";

export type CallbackStatus =
  | "promised"
  | "due_soon"
  | "overdue"
  | "kept"
  | "missed"
  | "recovered";

export type BookingStatus =
  | "requested"
  | "confirmed"
  | "rescheduled"
  | "cancelled"
  | "completed"
  | "no_show";

export type MessageType =
  | "human"
  | "pas"
  | "approval"
  | "assignment"
  | "evidence_reference"
  | "decision_record";

export type Role =
  | "broker_owner"
  | "admin"
  | "team_lead"
  | "agent"
  | "viewer"
  | "orvn_internal_admin";

export type Confidence = "observed" | "likely" | "uncertain";

export type CallOutcome =
  | "connected"
  | "voicemail"
  | "no_answer"
  | "scheduled_callback"
  | "appointment_set";

export type Sentiment = "positive" | "neutral" | "hesitant" | "negative";

export type EvidenceSource =
  | "call"
  | "signal"
  | "recommendation"
  | "proposal";

export type IntegrationCategory =
  | "crm"
  | "lead_source"
  | "calendar"
  | "communication"
  | "workspace";

export type MemoryStatus = "candidate" | "confirmed" | "dismissed";

export type CoverageStatus = "covered" | "stretched" | "gap";

export type ThreadObjectType =
  | "lead"
  | "callback"
  | "proposal"
  | "recommendation"
  | "booking"
  | "call"
  | "room";

// ─────────────────────────────────────────────────────────────────────────────
// People + access
// ─────────────────────────────────────────────────────────────────────────────

export interface Permission {
  key: string;
  label: string;
  allowed: boolean;
}

export interface RoleBundle {
  role: Role;
  label: string;
  description: string;
  permissions: Permission[];
}

export interface Agent extends DemoMeta {
  id: AgentId;
  name: string;
  role: Role;
  responseSpeedMs: number;
  callbacksOwned: number;
  activeLeads: number;
  coverageStatus: CoverageStatus;
  coachingFlags: string[];
  permissionsRole: Role;
}

export interface User extends DemoMeta {
  id: UserId;
  name: string;
  email: string;
  role: Role;
  status: "active" | "invited" | "suspended";
}

// ─────────────────────────────────────────────────────────────────────────────
// Operational objects
// ─────────────────────────────────────────────────────────────────────────────

export interface Lead extends DemoMeta {
  id: LeadId;
  source: string;
  ownerId: AgentId;
  stage: LeadStage;
  lastTouch: IsoTimestamp;
  riskLevel: Severity;
  nextAction: string;
  pasNote: string;
}

export interface Call extends DemoMeta {
  id: CallId;
  leadId: LeadId;
  agentId: AgentId;
  outcome: CallOutcome;
  transcriptPreview: string;
  objection: string;
  sentiment: Sentiment;
  evidenceIds: EvidenceId[];
  nextAction: string;
  occurredAt: IsoTimestamp;
}

export interface Callback extends DemoMeta {
  id: CallbackId;
  leadId: LeadId;
  ownerId: AgentId;
  sourceCallId: CallId;
  promisedAt: IsoTimestamp;
  dueAt: IsoTimestamp;
  status: CallbackStatus;
  riskLevel: Severity;
  proposedRecovery: string;
}

export interface Booking extends DemoMeta {
  id: BookingId;
  sourceLeadId: LeadId;
  agentId: AgentId;
  status: BookingStatus;
  evidenceIds: EvidenceId[];
  calendarState: string;
  scheduledAt: IsoTimestamp;
}

export interface PipelineRisk extends DemoMeta {
  id: RiskId;
  severity: Severity;
  reason: string;
  affectedLeadIds: LeadId[];
  suggestedRecovery: string;
}

export interface Recommendation extends DemoMeta {
  id: RecommendationId;
  title: string;
  evidenceIds: EvidenceId[];
  urgency: Severity;
  impact: string;
  possibleAction: string;
}

export interface ActionProposal extends DemoMeta {
  id: ProposalId;
  title: string;
  scope: string;
  status: ProposalStatus;
  expiresAt: IsoTimestamp;
  evidenceIds: EvidenceId[];
  actionPreview: string;
  auditLanguage: string;
}

export interface EvidenceSignal extends DemoMeta {
  id: EvidenceId;
  kind: string;
  source: EvidenceSource;
  summary: string;
  link: string;
}

// ─────────────────────────────────────────────────────────────────────────────
// Integrations
// ─────────────────────────────────────────────────────────────────────────────

export interface Integration extends DemoMeta {
  id: IntegrationId;
  name: string;
  category: IntegrationCategory;
  status: IntegrationStatus;
  readScope: string[];
  writeScope: string[];
  health: string;
  setupSteps: string[];
  lastSync: IsoTimestamp | null;
}

// ─────────────────────────────────────────────────────────────────────────────
// PAS Brain
// ─────────────────────────────────────────────────────────────────────────────

export interface MemoryCandidate extends DemoMeta {
  id: MemoryId;
  statement: string;
  confidence: Confidence;
  evidenceIds: EvidenceId[];
  status: MemoryStatus;
}

// ─────────────────────────────────────────────────────────────────────────────
// Notifications
// ─────────────────────────────────────────────────────────────────────────────

export interface Notification extends DemoMeta {
  id: NotificationId;
  severity: Severity;
  title: string;
  body: string;
  module: string;
  ts: IsoTimestamp;
  isRead: boolean;
  isDemoLabelled: true;
}

export interface NotificationReply extends DemoMeta {
  id: ReplyId;
  notificationId: NotificationId;
  text: string;
  capturedAt: IsoTimestamp;
}

// ─────────────────────────────────────────────────────────────────────────────
// Communication — PAS Room + object threads
// ─────────────────────────────────────────────────────────────────────────────

export interface RoomMessage extends DemoMeta {
  id: MessageId;
  threadId: ThreadId;
  authorType: "human" | "pas";
  authorId: string;
  type: MessageType;
  body: string;
  evidenceIds: EvidenceId[];
  ts: IsoTimestamp;
}

export interface ObjectThread extends DemoMeta {
  id: ThreadId;
  objectType: ThreadObjectType;
  objectId: string;
  messages: RoomMessage[];
}
