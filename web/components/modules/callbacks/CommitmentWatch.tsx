/*
 * CommitmentWatch — the flagship top section of /callbacks. Static, demo-only.
 * "PAS is watching the promises your brokerage made." All counts derive from
 * DEMO_CALLBACKS; proposed recovery actions from DEMO_PROPOSALS.
 */

import { DEMO_CALLBACKS, DEMO_PROPOSALS } from "@/lib/demo/operational";
import styles from "./callbacks.module.css";

export default function CommitmentWatch() {
  const overdue = DEMO_CALLBACKS.filter((cb) => cb.status === "overdue").length;
  const dueSoon = DEMO_CALLBACKS.filter((cb) => cb.status === "due_soon").length;
  const atRisk = DEMO_CALLBACKS.filter(
    (cb) => cb.riskLevel === "urgent" || cb.riskLevel === "critical",
  ).length;
  const recoveryCount = DEMO_PROPOSALS.length;

  const tiles = [
    { label: "Overdue", value: overdue, color: "var(--signal-urgent)" },
    { label: "Due soon", value: dueSoon, color: "var(--signal-attention)" },
    { label: "At risk", value: atRisk, color: "var(--signal-urgent)" },
    { label: "Recovery proposed", value: recoveryCount, color: "var(--signal-approval)" },
  ];

  return (
    <section className={styles.watch} aria-label="Commitment Watch">
      <div className={styles.watchHeader}>
        <h2 className={styles.watchTitle}>Commitment Watch</h2>
        <p className={styles.watchCopy}>
          PAS is watching the promises your brokerage made. Callback promises
          become operational objects, not memory.
        </p>
      </div>

      <div className={styles.watchGrid}>
        {tiles.map((tile) => (
          <div key={tile.label} className={styles.tile}>
            <span className={styles.tileTop}>
              <span
                className={styles.tileDot}
                style={{ background: tile.color }}
                aria-hidden="true"
              />
              <span className={styles.tileValue}>{tile.value}</span>
            </span>
            <span className={styles.tileLabel}>{tile.label}</span>
          </div>
        ))}
      </div>

      <div className={styles.recovery}>
        <p className={styles.recoveryHeading}>Proposed recovery actions</p>
        {DEMO_PROPOSALS.length === 0 ? (
          <p className={styles.recoveryEmpty}>No recovery proposed right now.</p>
        ) : (
          <ul className={styles.recoveryList}>
            {DEMO_PROPOSALS.map((proposal) => (
              <li key={proposal.id} className={styles.recoveryItem}>
                <span className={styles.recoveryTitle}>{proposal.title}</span>
                <span className={styles.recoveryMeta}>
                  {proposal.id} · {proposal.scope} · demo-only
                </span>
              </li>
            ))}
          </ul>
        )}
      </div>
    </section>
  );
}
