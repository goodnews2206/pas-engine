/*
 * CommandCenterOverview — the operating home. Static RSC, demo-only.
 * Synthesizes the operational demo layer (PR A–H) into one calm brief so a
 * broker owner can read the state of the brokerage in seconds.
 *
 * Hierarchy: brief → attention → commitments → proposals → coverage →
 * what PAS is learning → discussion → system health → evidence → ask PAS.
 * Every figure derives from the PR A model. No network, no live behavior.
 */

import OperatingBrief from "./OperatingBrief";
import TodayAttentionQueue from "./TodayAttentionQueue";
import CommitmentSnapshot from "./CommitmentSnapshot";
import ProposalSnapshot from "./ProposalSnapshot";
import AgentCoverageSnapshot from "./AgentCoverageSnapshot";
import RoomActivityPreview from "./RoomActivityPreview";
import IntegrationHealthSnapshot from "./IntegrationHealthSnapshot";
import EvidenceSnapshot from "./EvidenceSnapshot";
import BrainInsightStrip from "@/components/modules/pas-brain/BrainInsightStrip";
import styles from "./CommandCenterOverview.module.css";

export default function CommandCenterOverview() {
  return (
    <div className={styles.overview}>
      <OperatingBrief />

      {/* 1. What needs attention today */}
      <TodayAttentionQueue />

      {/* 2. Commitments + proposals */}
      <div className={styles.grid2}>
        <CommitmentSnapshot />
        <ProposalSnapshot />
      </div>

      {/* 3. Coverage + what PAS is learning */}
      <AgentCoverageSnapshot />
      <BrainInsightStrip />

      {/* 4. Discussion + system health */}
      <div className={styles.grid2}>
        <RoomActivityPreview />
        <IntegrationHealthSnapshot />
      </div>

      {/* 5. Evidence */}
      <EvidenceSnapshot />

      {/* Ask PAS entry point — Command Center §4.1 item 5 */}
      <section className={styles.askPas} aria-label="Ask PAS">
        <p className={styles.askPasHead}>Ask PAS anything</p>
        <p className={styles.askPasCopy}>
          Plain English. Typos are fine.{" "}
          <span className={styles.askPasExamples}>
            &ldquo;Which leads are slipping?&rdquo;&nbsp;&middot;&nbsp;&ldquo;What
            happened on the demo call?&rdquo;&nbsp;&middot;&nbsp;&ldquo;What needs
            attention?&rdquo;
          </span>
        </p>
        <span className={styles.askPasHint} aria-hidden="true">
          Use the composer below &darr;
        </span>
      </section>

      <p className={styles.disclaimer}>
        Demo/rehearsal data. PAS has not changed live customer behavior.
      </p>
    </div>
  );
}
