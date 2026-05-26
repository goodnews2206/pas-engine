/*
 * SystemStatusPanel — integration health at a glance.
 * Static RSC. Status is demo data only — not live integration state.
 */

import {
  SYSTEM_STATUS,
  type SystemStatusKind,
} from "@/lib/demo/commandCenter";
import styles from "./SystemStatusPanel.module.css";

const DOT_CLASSES: Record<SystemStatusKind, string> = {
  "healthy": styles.dotHealthy,
  "degraded": styles.dotDegraded,
  "disconnected": styles.dotDisconnected,
  "demo": styles.dotDemo,
};

const STATUS_LABELS: Record<SystemStatusKind, string> = {
  "healthy": "Healthy",
  "degraded": "Degraded",
  "disconnected": "Disconnected",
  "demo": "Demo",
};

const DETAIL_CLASSES: Record<SystemStatusKind, string> = {
  "healthy": "",
  "degraded": styles.detailDegraded,
  "disconnected": styles.detailCritical,
  "demo": "",
};

export default function SystemStatusPanel() {
  const hasIssues = SYSTEM_STATUS.some(
    (s) => s.status === "degraded" || s.status === "disconnected"
  );

  return (
    <section className={styles.section} aria-label="System status">
      <header className={styles.sectionHeader}>
        <h2 className={styles.sectionTitle}>System status</h2>
        {hasIssues && (
          <span className={styles.issueBadge} role="status">
            Attention required
          </span>
        )}
      </header>
      <ul className={styles.rows}>
        {SYSTEM_STATUS.map((item) => (
          <li key={item.id} className={styles.row}>
            <span
              className={`${styles.dot} ${DOT_CLASSES[item.status]}`}
              aria-label={`${item.service}: ${STATUS_LABELS[item.status]}`}
            />
            <span className={styles.service}>{item.service}</span>
            <span
              className={`${styles.detail} ${DETAIL_CLASSES[item.status]}`}
            >
              {item.detail}
            </span>
          </li>
        ))}
      </ul>
      <p className={styles.disclaimer}>
        PAS has not changed live customer behavior.
      </p>
    </section>
  );
}
