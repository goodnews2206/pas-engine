/*
 * PasBrainOverview — the first-class PAS Brain surface. Static RSC, demo-only.
 * Answers: what PAS knows · what it is learning · what you can ask · what it
 * does not know yet · what evidence supports it · how confident it is.
 * No real search, no vector DB, no persistence.
 */

import {
  DEMO_MEMORY_CANDIDATES,
  DEMO_EVIDENCE,
  DEMO_BRAIN_UNKNOWNS,
} from "@/lib/demo/operational";
import ContinuityMetricStrip from "@/components/modules/continuity/ContinuityMetricStrip";
import BrainInsightStrip from "./BrainInsightStrip";
import MemoryCandidateCard from "./MemoryCandidateCard";
import BrainQueryExamples from "./BrainQueryExamples";
import BrainUnknownsPanel from "./BrainUnknownsPanel";
import BrainEvidencePanel from "./BrainEvidencePanel";
import styles from "./PasBrainOverview.module.css";

export default function PasBrainOverview() {
  const observed = DEMO_MEMORY_CANDIDATES.filter(
    (m) => m.confidence === "observed",
  ).length;

  return (
    <>
      <header className={styles.header}>
        <div className={styles.headerTop}>
          <h1 className={styles.title}>PAS Brain</h1>
          <span className={styles.demoPill}>Simulated</span>
        </div>
        <p className={styles.intro}>
          PAS is forming operational memory from repeated signals. A human
          decides what becomes trusted brokerage knowledge — PAS only claims what
          it can support with evidence.
        </p>
        <p className={styles.rehearsalNote}>
          Rehearsal mode — this memory is simulated, not learned from live
          activity.
        </p>
      </header>

      <BrainInsightStrip limit={3} />

      <ContinuityMetricStrip
        ariaLabel="PAS Brain summary"
        metrics={[
          { label: "Candidate memories", value: DEMO_MEMORY_CANDIDATES.length },
          { label: "Observed", value: observed, tone: "fyi" },
          { label: "Evidence signals", value: DEMO_EVIDENCE.length },
          {
            label: "Known gaps",
            value: DEMO_BRAIN_UNKNOWNS.length,
            tone: "attention",
          },
        ]}
      />

      <section className={styles.panel} aria-label="Memory candidates">
        <div className={styles.panelHeader}>
          <h2 className={styles.panelTitle}>Memory PAS is forming</h2>
          <p className={styles.panelDesc}>
            Candidate memories from repeated signals. Each one is evidence-backed
            and waits for a human to confirm it as trusted knowledge.
          </p>
        </div>
        <div className={styles.grid}>
          {DEMO_MEMORY_CANDIDATES.map((candidate) => (
            <MemoryCandidateCard key={candidate.id} candidate={candidate} />
          ))}
        </div>
      </section>

      <BrainQueryExamples />
      <BrainUnknownsPanel />
      <BrainEvidencePanel />

      <p className={styles.disclaimer}>
        This is demo/rehearsal data. PAS has not changed live customer behavior.
      </p>
    </>
  );
}
