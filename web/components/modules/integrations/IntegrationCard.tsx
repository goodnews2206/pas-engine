/*
 * IntegrationCard — one connector in the marketplace. Clickable (opens the
 * detail drawer). Demo-only. Status is never colour alone: dot + labelled chip.
 */

import type { Integration } from "@/lib/demo/operational";
import { STATUS_META, TONE_COLORS, CATEGORY_META, formatSync } from "./meta";
import styles from "./IntegrationCard.module.css";

interface Props {
  integration: Integration;
  onOpen: (integration: Integration) => void;
}

export default function IntegrationCard({ integration, onOpen }: Props) {
  const status = STATUS_META[integration.status];
  const category = CATEGORY_META[integration.category];
  const hasWrite = integration.writeScope.length > 0;

  return (
    <button
      type="button"
      className={styles.card}
      onClick={() => onOpen(integration)}
      aria-label={`${integration.name} — ${status.label}. Open details.`}
    >
      <div className={styles.headerRow}>
        <span className={styles.name}>{integration.name}</span>
        <span className={styles.demoPill}>Simulated</span>
      </div>

      <div className={styles.metaRow}>
        <span className={styles.categoryBadge}>{category.label}</span>
        <span className={styles.statusChip}>
          <span
            className={styles.dot}
            style={{ background: TONE_COLORS[status.tone] }}
            aria-hidden="true"
          />
          {status.label}
        </span>
      </div>

      <p className={styles.use}>{category.use}</p>

      <dl className={styles.scopes}>
        <div className={styles.scopeRow}>
          <dt className={styles.scopeLabel}>Reads</dt>
          <dd className={styles.scopeValue}>
            {integration.readScope.length > 0
              ? integration.readScope.join(", ")
              : "—"}
          </dd>
        </div>
        <div className={styles.scopeRow}>
          <dt className={styles.scopeLabel}>Writes</dt>
          <dd className={styles.scopeValue}>
            {hasWrite ? "Approval required" : "None"}
          </dd>
        </div>
      </dl>

      <div className={styles.footer}>
        <span className={styles.health}>{integration.health}</span>
        <span className={styles.sync}>Last sync: {formatSync(integration.lastSync)}</span>
      </div>
    </button>
  );
}
