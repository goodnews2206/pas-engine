/*
 * IntegrationHealthPanel — at-a-glance connection health across the
 * marketplace. Static, demo-only. Counts derive from DEMO_INTEGRATIONS.
 */

import {
  DEMO_INTEGRATIONS,
  type IntegrationStatus,
} from "@/lib/demo/operational";
import { STATUS_META, TONE_COLORS } from "./meta";
import styles from "./IntegrationsOverview.module.css";

const ORDER: IntegrationStatus[] = [
  "connected_read_only",
  "write_approval_required",
  "degraded",
  "not_connected",
];

export default function IntegrationHealthPanel() {
  const counts: Record<IntegrationStatus, number> = {
    connected_read_only: 0,
    write_approval_required: 0,
    degraded: 0,
    not_connected: 0,
  };
  for (const integration of DEMO_INTEGRATIONS) {
    counts[integration.status] += 1;
  }

  return (
    <section className={styles.panel} aria-label="Connection health">
      <h2 className={styles.panelTitle}>Connection health</h2>
      <div className={styles.healthRow}>
        {ORDER.map((status) => {
          const meta = STATUS_META[status];
          return (
            <div key={status} className={styles.healthStat}>
              <span className={styles.healthValue}>{counts[status]}</span>
              <span className={styles.healthLabel}>
                <span
                  className={styles.dot}
                  style={{ background: TONE_COLORS[meta.tone] }}
                  aria-hidden="true"
                />
                {meta.label}
              </span>
            </div>
          );
        })}
      </div>
    </section>
  );
}
