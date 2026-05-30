/*
 * CommitmentSnapshot — callbacks at risk (the flagship commitment view, in
 * brief). Static RSC, demo-only. Links to /callbacks.
 */

import Link from "next/link";
import { DEMO_CALLBACKS, DEMO_AGENTS } from "@/lib/demo/operational";
import styles from "./CommandCenterOverview.module.css";

const AGENT_NAMES: Record<string, string> = Object.fromEntries(
  DEMO_AGENTS.map((a) => [a.id, a.name]),
);

export default function CommitmentSnapshot() {
  const overdue = DEMO_CALLBACKS.filter((c) => c.status === "overdue");
  const dueSoon = DEMO_CALLBACKS.filter((c) => c.status === "due_soon").length;
  const atRisk = DEMO_CALLBACKS.filter(
    (c) => c.riskLevel === "urgent" || c.riskLevel === "critical",
  ).length;

  const overdueOwners = [...new Set(overdue.map((c) => c.ownerId))].map(
    (id) => AGENT_NAMES[id] ?? id,
  );

  const tiles = [
    { label: "Overdue", value: overdue.length, color: "var(--signal-urgent)" },
    { label: "Due soon", value: dueSoon, color: "var(--signal-attention)" },
    { label: "At risk", value: atRisk, color: "var(--signal-urgent)" },
  ];

  return (
    <section className={styles.snapshot} aria-label="Commitments at risk">
      <div className={styles.snapshotHeader}>
        <h2 className={styles.snapshotTitle}>Commitments at risk</h2>
        <Link href="/callbacks" className={styles.moduleLink}>
          Commitment Watch →
        </Link>
      </div>
      <p className={styles.snapshotLead}>
        {overdueOwners.length > 0
          ? `${overdueOwners.length === 1 ? "One agent is" : `${overdueOwners.length} agents are`} carrying overdue callback risk — ${overdueOwners.join(", ")}.`
          : "Every callback promise is on track right now."}
      </p>
      <div className={styles.tiles}>
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
    </section>
  );
}
