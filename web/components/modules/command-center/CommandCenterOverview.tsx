/*
 * CommandCenterOverview — assembles all Command Center sections in order.
 * Dashboard IA §4.1: attention → proposals → pipeline → status → evidence → ask PAS.
 * Static RSC. No client state.
 */

import CommandCenterHeader from "./CommandCenterHeader";
import AttentionSummary from "./AttentionSummary";
import RecommendationPreview from "./RecommendationPreview";
import PipelineSnapshot from "./PipelineSnapshot";
import SystemStatusPanel from "./SystemStatusPanel";
import EvidencePreview from "./EvidencePreview";
import BrainInsightStrip from "@/components/modules/pas-brain/BrainInsightStrip";
import styles from "./CommandCenterOverview.module.css";

export default function CommandCenterOverview() {
  return (
    <div className={styles.overview}>
      <CommandCenterHeader />
      <AttentionSummary />
      <RecommendationPreview />
      <PipelineSnapshot />
      <SystemStatusPanel />
      <EvidencePreview />

      {/* Compact PAS Brain strip — a strip, not a redesign */}
      <BrainInsightStrip />

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
    </div>
  );
}
