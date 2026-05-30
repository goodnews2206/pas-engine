/*
 * AgentCoveragePanel — at-a-glance team coverage. Static RSC, demo-only.
 * Answers "where is coverage weak?" from the agent roster.
 */

import { DEMO_AGENTS, type CoverageStatus } from "@/lib/demo/operational";
import styles from "./AgentsOverview.module.css";

const COVERAGE_META: Record<
  CoverageStatus,
  { label: string; color: string }
> = {
  covered: { label: "Available", color: "var(--signal-fyi)" },
  stretched: { label: "Stretched", color: "var(--signal-attention)" },
  gap: { label: "Coverage gap", color: "var(--signal-urgent)" },
};

const ORDER: CoverageStatus[] = ["covered", "stretched", "gap"];

export default function AgentCoveragePanel() {
  const counts: Record<CoverageStatus, number> = {
    covered: 0,
    stretched: 0,
    gap: 0,
  };
  for (const agent of DEMO_AGENTS) {
    counts[agent.coverageStatus] += 1;
  }

  return (
    <section className={styles.panel} aria-label="Team coverage">
      <h2 className={styles.panelTitle}>Team coverage</h2>
      <div className={styles.coverageRow}>
        {ORDER.map((status) => {
          const meta = COVERAGE_META[status];
          return (
            <div key={status} className={styles.coverageStat}>
              <span className={styles.coverageStatValue}>{counts[status]}</span>
              <span className={styles.coverageStatLabel}>
                <span
                  className={styles.dot}
                  style={{ background: meta.color }}
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
