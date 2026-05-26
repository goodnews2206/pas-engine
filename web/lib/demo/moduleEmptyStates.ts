/*
 * Module-specific empty state copy for all skeleton routes.
 * All content is rehearsal/demo only — no live data, no live claims.
 * Authority: docs/pas_web_foundation_v1.md §Step 9
 *            docs/pas_product_design_book.md §2 §4
 */

export interface ModuleEmptyState {
  id: string;
  /** One or two sentences explaining what this surface helps with in daily ops. */
  contextCopy: string;
  /** What PAS can eventually answer here — plain-English questions, rendered as a list. */
  readonly pasCanAnswer: readonly string[];
  /** What is intentionally not connected in this rehearsal snapshot — rendered as a list. */
  readonly notConnectedYet: readonly string[];
  demoOnly: true;
  noLiveBehavior: true;
}

const STATES: readonly ModuleEmptyState[] = [
  {
    id: "leads",
    contextCopy:
      "This is where PAS will show lead context, source, ownership, current pipeline status, and next best action — one view for the full picture of who is in your pipeline and where they stand.",
    pasCanAnswer: [
      "Which leads have gone quiet?",
      "Who needs a follow-up today?",
      "Where did this lead come from?",
      "What is the next best action for this contact?",
      "Which leads are closest to booking?",
    ],
    notConnectedYet: [
      "Lead source integrations (Zillow, Realtor.com, Facebook)",
      "CRM adapter",
      "PAS Brain qualification scoring",
      "Lead assignment rules",
    ],
    demoOnly: true,
    noLiveBehavior: true,
  },
  {
    id: "calls",
    contextCopy:
      "This is where PAS will surface every call — transcript, outcome, FSM state trace, and the evidence behind the conversation. No more hunting through recordings for what was said.",
    pasCanAnswer: [
      "What was said on the last call?",
      "Did the agent follow the script?",
      "Were there any red flags in this conversation?",
      "What did the lead say about their timeline?",
      "Which calls need a coaching review?",
    ],
    notConnectedYet: [
      "Twilio live call routing",
      "Deepgram transcription pipeline",
      "ElevenLabs voice layer",
      "PAS Brain tone and objection model",
    ],
    demoOnly: true,
    noLiveBehavior: true,
  },
  {
    id: "callbacks",
    contextCopy:
      "This is where PAS will track every callback promise — who said they would call back, when they were supposed to, and whether it happened. Overdue callbacks surface automatically.",
    pasCanAnswer: [
      "Which callbacks are overdue?",
      "Who owns this callback?",
      "Was a callback promised on this call?",
      "Which agents have the most missed callbacks?",
    ],
    notConnectedYet: [
      "PAS callback capture flow (PAS128)",
      "Notification delivery for overdue callbacks",
      "Calendar sync and availability check",
    ],
    demoOnly: true,
    noLiveBehavior: true,
  },
  {
    id: "bookings",
    contextCopy:
      "This is where PAS will show Cal.com-backed appointments — confirmation status, agent assignment, and the evidence from the call that led to the booking.",
    pasCanAnswer: [
      "Which bookings are at risk?",
      "Is this agent available for this appointment?",
      "Was this lead qualified before booking?",
      "Which bookings came from warm vs. cold leads?",
    ],
    notConnectedYet: [
      "Cal.com integration",
      "Agent calendar sync",
      "Booking confirmation webhooks",
      "Pre-meeting qualification check",
    ],
    demoOnly: true,
    noLiveBehavior: true,
  },
  {
    id: "pipeline-risks",
    contextCopy:
      "This is where PAS will flag which leads and deals are at risk of stalling — surfaced by pattern, not by manually reviewing every contact.",
    pasCanAnswer: [
      "Which deals are about to go cold?",
      "What is the risk reason for this lead?",
      "What was the last known touch on this deal?",
      "What would recover this lead?",
    ],
    notConnectedYet: [
      "Proactive Observer (PAS205)",
      "Live CRM data connection",
      "Pipeline scoring model",
      "Risk threshold configuration",
    ],
    demoOnly: true,
    noLiveBehavior: true,
  },
  {
    id: "recommendations",
    contextCopy:
      "This is where PAS will surface what it thinks should happen next — each recommendation backed by evidence from calls, callbacks, and pipeline signals.",
    pasCanAnswer: [
      "Why is PAS recommending this?",
      "What evidence supports this recommendation?",
      "How urgent is this recommendation?",
      "What happens if we do not act?",
    ],
    notConnectedYet: [
      "Action Proposals (PAS209)",
      "Evidence Digest wiring",
      "Approval routing",
      "PAS208 live recommendation engine",
    ],
    demoOnly: true,
    noLiveBehavior: true,
  },
  {
    id: "action-proposals",
    contextCopy:
      "This is where PAS will present bounded, named actions it would like to take — nothing happens until a human approves. Every proposal includes what will be done, why, and what the approval window is.",
    pasCanAnswer: [
      "What action is PAS proposing?",
      "What evidence drove this proposal?",
      "What happens if I approve?",
      "Has this action window lapsed?",
    ],
    notConnectedYet: [
      "PAS209 bounded action layer",
      "Integration write paths (CRM, Cal.com, SMS)",
      "Approval and rejection audit trail",
      "Proposal expiry countdown",
    ],
    demoOnly: true,
    noLiveBehavior: true,
  },
  {
    id: "evidence-digest",
    contextCopy:
      "This is where PAS will show its receipts — every claim linked to the transcript, snapshot, or signal that justified it. Evidence is always available, never hidden.",
    pasCanAnswer: [
      "Why did PAS say that?",
      "What was the source for this recommendation?",
      "How confident is PAS in this signal?",
      "Where did this evidence come from?",
    ],
    notConnectedYet: [
      "Audit log surface",
      "Linked transcript viewer",
      "PAS201–PAS203 evidence chain",
      "Evidence export and external review",
    ],
    demoOnly: true,
    noLiveBehavior: true,
  },
  {
    id: "simulation-lab",
    contextCopy:
      "This is where operators will run rehearsal calls, scenarios, and recommendations with zero live side effects. Every artifact is clearly marked as rehearsal and cannot trigger production behavior.",
    pasCanAnswer: [
      "What would happen if PAS handled this scenario?",
      "How would PAS respond to this objection?",
      "Can we rehearse this edge case before it happens live?",
      "What does the evidence trail look like for this simulation?",
    ],
    notConnectedYet: [
      "Simulation runner engine",
      "Voice simulation (ElevenLabs)",
      "Cal.com rehearsal mode",
      "Scenario library and scenario export",
    ],
    demoOnly: true,
    noLiveBehavior: true,
  },
  {
    id: "integrations",
    contextCopy:
      "This is where brokerages will connect CRM, Gmail, Google Workspace, Slack, and lead sources. Read access always comes first. Write access requires explicit approval per scope — PAS never takes write access it has not been given.",
    pasCanAnswer: [
      "What can PAS answer with this connection?",
      "Is this integration healthy?",
      "When did PAS last sync from this source?",
      "Which permissions has PAS been granted here?",
    ],
    notConnectedYet: [
      "OAuth and API key connect flows",
      "CRM adapter (Salesforce, Follow Up Boss, HubSpot)",
      "Cal.com, Twilio, Deepgram, ElevenLabs connectors",
      "Lead source integrations (Zillow, Realtor.com, Facebook)",
    ],
    demoOnly: true,
    noLiveBehavior: true,
  },
  {
    id: "settings",
    contextCopy:
      "This is where workspace roles, permissions, notification rules, and PAS behavior policies will be managed. Configuration is brokerage-specific — PAS adapts to how your office works, not the other way around.",
    pasCanAnswer: [
      "Who has access to what in this workspace?",
      "What is PAS allowed to do for this brokerage?",
      "What are the operational hours for this office?",
      "What tone and disclosure rules apply?",
    ],
    notConnectedYet: [
      "Settings persistence layer",
      "PAS Brain configuration (tone, scripts, disclosures)",
      "Member management and role assignment",
      "API key rotation and audit",
    ],
    demoOnly: true,
    noLiveBehavior: true,
  },
];

export const MODULE_EMPTY_STATES: Readonly<Record<string, ModuleEmptyState>> =
  Object.fromEntries(STATES.map((s) => [s.id, s]));
