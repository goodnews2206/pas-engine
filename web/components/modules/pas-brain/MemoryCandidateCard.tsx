/*
 * MemoryCandidateCard — one candidate memory PAS is forming. Static, demo-only.
 * A human decides what becomes trusted brokerage knowledge.
 */

import type { MemoryCandidate, MemoryStatus } from "@/lib/demo/operational";
import EvidenceMiniList from "@/components/modules/continuity/EvidenceMiniList";
import ConfidenceLabel, { CONFIDENCE_META } from "./ConfidenceLabel";
import styles from "./PasBrainOverview.module.css";

const STATUS_LABELS: Record<MemoryStatus, string> = {
  candidate: "Candidate memory",
  confirmed: "Confirmed",
  dismissed: "Dismissed",
};

interface Props {
  candidate: MemoryCandidate;
}

export default function MemoryCandidateCard({ candidate }: Props) {
  return (
    <article className={styles.memoryCard}>
      <div className={styles.memoryTop}>
        <ConfidenceLabel confidence={candidate.confidence} />
        <span className={styles.statusChip}>
          {STATUS_LABELS[candidate.status]}
        </span>
      </div>
      <p className={styles.memoryStatement}>{candidate.statement}</p>
      <p className={styles.memoryNote}>
        {CONFIDENCE_META[candidate.confidence].note} A human decides whether this
        becomes trusted brokerage knowledge.
      </p>
      <div>
        <p className={styles.evidenceLabel}>Evidence</p>
        <EvidenceMiniList evidenceIds={candidate.evidenceIds} />
      </div>
    </article>
  );
}
