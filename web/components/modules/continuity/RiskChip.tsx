/*
 * RiskChip — severity as dot + label (never colour alone). Static, demo-only.
 */

import type { Severity } from "@/lib/demo/operational";
import { SEVERITY_META } from "./severity";
import styles from "./continuity.module.css";

interface Props {
  severity: Severity;
  label?: string;
}

export default function RiskChip({ severity, label }: Props) {
  const meta = SEVERITY_META[severity];
  return (
    <span
      className={styles.chip}
      style={{ color: meta.color, background: meta.bg }}
    >
      <span
        className={styles.chipDot}
        style={{ background: meta.color }}
        aria-hidden="true"
      />
      {label ?? meta.label}
    </span>
  );
}
