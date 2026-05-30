/*
 * Continuity severity + format helpers. Display-only.
 * Maps the model's Severity vocabulary to calm labels + colour tokens.
 * Severity is never colour alone — callers pair this with a label + text.
 */

import type { Severity } from "@/lib/demo/operational";

export const SEVERITY_META: Record<
  Severity,
  { label: string; color: string; bg: string }
> = {
  fyi: { label: "FYI", color: "var(--signal-fyi)", bg: "var(--signal-fyi-bg)" },
  needs_attention: {
    label: "Needs attention",
    color: "var(--signal-attention)",
    bg: "var(--signal-attention-bg)",
  },
  urgent: {
    label: "Urgent",
    color: "var(--signal-urgent)",
    bg: "var(--signal-urgent-bg)",
  },
  approval_required: {
    label: "Approval required",
    color: "var(--signal-approval)",
    bg: "var(--signal-approval-bg)",
  },
  critical: {
    label: "Critical",
    color: "var(--signal-critical)",
    bg: "var(--signal-critical-bg)",
  },
};

export function railColorForSeverity(severity: Severity): string {
  return SEVERITY_META[severity].color;
}

/** Deterministic ISO formatter — no Date object (avoids SSR/locale drift). */
export function formatIso(iso: string | null): string {
  if (!iso) return "—";
  const [date, rest] = iso.replace("Z", "").split("T");
  const time = rest ? rest.slice(0, 5) : "";
  return time ? `${date} · ${time} UTC` : date;
}
