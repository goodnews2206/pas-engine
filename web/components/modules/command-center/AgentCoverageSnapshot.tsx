/*
 * AgentCoverageSnapshot — who needs coverage. Static RSC, demo-only.
 * Links to /agents.
 */

import Link from "next/link";
import {
  DEMO_AGENTS,
  type CoverageStatus,
} from "@/lib/demo/operational";
import styles from "./CommandCenterOverview.module.css";

const META: Record<CoverageStatus, { label: string; color: string }> = {
  covered: { label: "Available", color: "var(--signal-fyi)" },
  stretched: { label: "Stretched", color: "var(--signal-attention)" },
  gap: { label: "Coverage gap", color: "var(--signal-urgent)" },
};

const ORDER: CoverageStatus[] = ["covered", "stretched", "gap"];

export default function AgentCoverageSnapshot() {
  const counts: Record<CoverageStatus, number> = {
    covered: 0,
    stretched: 0,
    gap: 0,
  };
  for (const agent of DEMO_AGENTS) counts[agent.coverageStatus] += 1;

  const needCoverage = DEMO_AGENTS.filter(
    (a) => a.coverageStatus !== "covered",
  ).map((a) => a.name);

  return (
    <section className={styles.snapshot} aria-label="Who needs coverage">
      <div className={styles.snapshotHeader}>
        <h2 className={styles.snapshotTitle}>Who needs coverage</h2>
        <Link href="/agents" className={styles.moduleLink}>
          Agents →
        </Link>
      </div>
      <p className={styles.snapshotLead}>
        {needCoverage.length > 0
          ? `${needCoverage.length} of ${DEMO_AGENTS.length} are stretched or have a coverage gap — ${needCoverage.join(", ")}.`
          : "The whole team has healthy coverage right now."}
      </p>
      <div className={styles.tiles}>
        {ORDER.map((status) => (
          <div key={status} className={styles.tile}>
            <span className={styles.tileTop}>
              <span
                className={styles.tileDot}
                style={{ background: META[status].color }}
                aria-hidden="true"
              />
              <span className={styles.tileValue}>{counts[status]}</span>
            </span>
            <span className={styles.tileLabel}>{META[status].label}</span>
          </div>
        ))}
      </div>
    </section>
  );
}
