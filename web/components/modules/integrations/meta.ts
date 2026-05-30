/*
 * Integrations UI metadata + formatters. Display-only helpers — not data.
 * Per-integration data lives in the PR A model (DEMO_INTEGRATIONS); this file
 * only maps the model's closed vocabularies to calm broker-facing labels.
 */

import type {
  IntegrationStatus,
  IntegrationCategory,
} from "@/lib/demo/operational";

export type StatusTone = "connected" | "approval" | "degraded" | "off";

export const STATUS_META: Record<
  IntegrationStatus,
  { label: string; tone: StatusTone }
> = {
  connected_read_only: { label: "Read-only", tone: "connected" },
  write_approval_required: { label: "Write needs approval", tone: "approval" },
  degraded: { label: "Degraded", tone: "degraded" },
  not_connected: { label: "Not connected", tone: "off" },
};

export const TONE_COLORS: Record<StatusTone, string> = {
  connected: "var(--signal-fyi)",
  approval: "var(--signal-attention)",
  degraded: "var(--signal-urgent)",
  off: "var(--ink-disabled)",
};

export const CATEGORY_META: Record<
  IntegrationCategory,
  { label: string; use: string }
> = {
  crm: {
    label: "CRM",
    use: "Reads contacts, deals and activity so PAS can answer pipeline questions.",
  },
  lead_source: {
    label: "Lead source",
    use: "Brings inbound leads in so PAS can watch first response.",
  },
  calendar: {
    label: "Calendar / booking",
    use: "Sees availability and bookings so PAS can protect appointments.",
  },
  communication: {
    label: "Communication",
    use: "Reads conversations for context. Sending always needs approval.",
  },
  workspace: {
    label: "Workspace",
    use: "Reads shared docs and sheets so PAS can reference your records.",
  },
};

export const CATEGORY_ORDER: IntegrationCategory[] = [
  "crm",
  "lead_source",
  "calendar",
  "communication",
  "workspace",
];

/** Deterministic ISO formatter — no Date object (avoids SSR/locale drift). */
export function formatSync(iso: string | null): string {
  if (!iso) return "Never";
  const [date, rest] = iso.replace("Z", "").split("T");
  const time = rest ? rest.slice(0, 5) : "";
  return time ? `${date} · ${time} UTC` : date;
}

export const CONNECTION_NOTES: Record<IntegrationStatus, string> = {
  not_connected:
    "Not connected yet. Connecting always starts with read-only access.",
  connected_read_only:
    "Connected for reading only. PAS can answer questions but cannot change anything.",
  write_approval_required:
    "Read access is active. Any write is prepared for your approval first — nothing sends on its own.",
  degraded:
    "Connected, but the feed is delayed. PAS may be working with slightly stale data.",
};
