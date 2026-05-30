/*
 * BrainEvidencePanel — the receipts behind PAS's memory, grouped by source.
 * Static, demo-only. Summaries only — no raw transcript dumps.
 */

import {
  DEMO_EVIDENCE,
  type EvidenceSource,
} from "@/lib/demo/operational";
import styles from "./PasBrainOverview.module.css";

const SOURCE_LABELS: Record<EvidenceSource, string> = {
  call: "Call evidence",
  signal: "Observed signals",
  recommendation: "Recommendation basis",
  proposal: "Proposal basis",
};

const SOURCE_ORDER: EvidenceSource[] = [
  "call",
  "signal",
  "recommendation",
  "proposal",
];

export default function BrainEvidencePanel() {
  const groups = SOURCE_ORDER.map((source) => ({
    source,
    label: SOURCE_LABELS[source],
    items: DEMO_EVIDENCE.filter((e) => e.source === source),
  })).filter((g) => g.items.length > 0);

  return (
    <section className={styles.panel} aria-label="Evidence behind PAS memory">
      <div className={styles.panelHeader}>
        <h2 className={styles.panelTitle}>Evidence behind the memory</h2>
        <p className={styles.panelDesc}>
          Every belief PAS forms points back to a receipt. Summaries only — open
          a receipt to see the full source.
        </p>
      </div>
      {groups.map((group) => (
        <div key={group.source} className={styles.evidenceGroup}>
          <p className={styles.evidenceGroupTitle}>{group.label}</p>
          {group.items.map((evidence) => (
            <div key={evidence.id} className={styles.evidenceRow}>
              <a className={styles.evidenceId} href={evidence.link}>
                {evidence.id}
              </a>
              <span className={styles.evidenceSummary}>{evidence.summary}</span>
            </div>
          ))}
        </div>
      ))}
    </section>
  );
}
