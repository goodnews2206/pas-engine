/*
 * ConfidenceLabel — plain-English confidence, never numeric false precision.
 * Static, demo-only.
 */

import type { Confidence } from "@/lib/demo/operational";
import styles from "./PasBrainOverview.module.css";

export const CONFIDENCE_META: Record<
  Confidence,
  { label: string; note: string; color: string; bg: string }
> = {
  observed: {
    label: "Observed",
    note: "PAS has seen this directly.",
    color: "var(--signal-fyi)",
    bg: "var(--signal-fyi-bg)",
  },
  likely: {
    label: "Likely",
    note: "Enough evidence to suggest it.",
    color: "var(--signal-attention)",
    bg: "var(--signal-attention-bg)",
  },
  uncertain: {
    label: "Still uncertain",
    note: "Not enough evidence yet.",
    color: "var(--ink-muted)",
    bg: "var(--surface-subtle)",
  },
};

interface Props {
  confidence: Confidence;
}

export default function ConfidenceLabel({ confidence }: Props) {
  const meta = CONFIDENCE_META[confidence];
  return (
    <span
      className={styles.confidence}
      style={{ color: meta.color, background: meta.bg }}
    >
      <span
        className={styles.confDot}
        style={{ background: meta.color }}
        aria-hidden="true"
      />
      {meta.label}
    </span>
  );
}
