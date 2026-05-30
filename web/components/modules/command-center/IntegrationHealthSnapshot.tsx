/*
 * IntegrationHealthSnapshot — are the systems healthy. Static RSC, demo-only.
 * Links to /integrations.
 */

import Link from "next/link";
import { DEMO_INTEGRATIONS } from "@/lib/demo/operational";
import styles from "./CommandCenterOverview.module.css";

export default function IntegrationHealthSnapshot() {
  const connected = DEMO_INTEGRATIONS.filter(
    (i) => i.status === "connected_read_only" || i.status === "write_approval_required",
  ).length;
  const degraded = DEMO_INTEGRATIONS.filter((i) => i.status === "degraded");
  const notConnected = DEMO_INTEGRATIONS.filter(
    (i) => i.status === "not_connected",
  ).length;

  const tiles = [
    { label: "Connected", value: connected, color: "var(--signal-fyi)" },
    { label: "Degraded", value: degraded.length, color: "var(--signal-urgent)" },
    { label: "Not connected", value: notConnected, color: "var(--ink-disabled)" },
  ];

  return (
    <section className={styles.snapshot} aria-label="System health">
      <div className={styles.snapshotHeader}>
        <h2 className={styles.snapshotTitle}>System health</h2>
        <Link href="/integrations" className={styles.moduleLink}>
          Integrations →
        </Link>
      </div>
      <p className={styles.snapshotLead}>
        {degraded.length > 0
          ? `${degraded.length} connection ${degraded.length === 1 ? "is" : "are"} degraded — ${degraded.map((d) => d.name).join(", ")}.`
          : "All connected systems are healthy."}
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
