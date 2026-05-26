/*
 * AttentionSummary — ordered list of items waiting on the user, by severity.
 * Dashboard IA §4.1 item 1. Static RSC.
 * Severity is NEVER colour alone: each item uses rail + chip + label.
 */

import {
  ATTENTION_ITEMS,
  type AttentionSeverity,
} from "@/lib/demo/commandCenter";
import styles from "./AttentionSummary.module.css";

const SEVERITY_LABELS: Record<AttentionSeverity, string> = {
  "critical": "Critical",
  "urgent": "Urgent",
  "approval-required": "Approval required",
  "needs-attention": "Needs attention",
};

const RAIL_COLORS: Record<AttentionSeverity, string> = {
  "critical": "var(--signal-critical)",
  "urgent": "var(--signal-urgent)",
  "approval-required": "var(--signal-approval)",
  "needs-attention": "var(--signal-attention)",
};

const CHIP_CLASSES: Record<AttentionSeverity, string> = {
  "critical": styles.chipCritical,
  "urgent": styles.chipUrgent,
  "approval-required": styles.chipApproval,
  "needs-attention": styles.chipAttention,
};

export default function AttentionSummary() {
  return (
    <section className={styles.section} aria-label="Needs your attention">
      <header className={styles.sectionHeader}>
        <h2 className={styles.sectionTitle}>Needs your attention</h2>
        <span
          className={styles.countBadge}
          aria-label={`${ATTENTION_ITEMS.length} items`}
        >
          {ATTENTION_ITEMS.length}
        </span>
      </header>
      <ul className={styles.items}>
        {ATTENTION_ITEMS.map((item) => (
          <li key={item.id} className={styles.item}>
            <div
              className={styles.rail}
              style={{ background: RAIL_COLORS[item.severity] }}
              aria-hidden="true"
            />
            <div className={styles.itemBody}>
              <div className={styles.itemMeta}>
                <span
                  className={`${styles.chip} ${CHIP_CLASSES[item.severity]}`}
                >
                  {SEVERITY_LABELS[item.severity]}
                </span>
              </div>
              <p className={styles.itemTitle}>{item.title}</p>
              <p className={styles.itemText}>{item.body}</p>
              <div className={styles.itemFooter}>
                <span className={styles.evidenceHint}>
                  {item.evidenceLabel}
                </span>
                <a href={item.actionHref} className={styles.actionLink}>
                  {item.actionLabel}
                </a>
              </div>
            </div>
          </li>
        ))}
      </ul>
      <p className={styles.disclaimer}>
        PAS has not changed live customer behavior.
      </p>
    </section>
  );
}
