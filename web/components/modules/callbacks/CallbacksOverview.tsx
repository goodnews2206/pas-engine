/*
 * CallbacksOverview — the flagship /callbacks surface. Static RSC, demo-only.
 * "PAS watches commitments." Consumes DEMO_CALLBACKS + DEMO_LEADS + DEMO_CALLS
 * + DEMO_PROPOSALS + DEMO_EVIDENCE, resolving relations by id.
 */

import {
  DEMO_CALLBACKS,
  DEMO_PROPOSALS,
  DEMO_EVIDENCE,
  type ActionProposal,
} from "@/lib/demo/operational";
import ContinuityHeader from "@/components/modules/continuity/ContinuityHeader";
import CommitmentWatch from "./CommitmentWatch";
import CallbackCard from "./CallbackCard";
import continuity from "@/components/modules/continuity/continuity.module.css";

/** Evidence whose summary/link references this callback id. */
function evidenceForCallback(callbackId: string): string[] {
  return DEMO_EVIDENCE.filter(
    (e) => e.summary.includes(callbackId) || e.link.includes(callbackId),
  ).map((e) => e.id);
}

/** A recovery proposal that names this callback id. */
function proposalForCallback(callbackId: string): ActionProposal | null {
  return (
    DEMO_PROPOSALS.find((p) =>
      [p.title, p.actionPreview, p.scope].some((s) => s.includes(callbackId)),
    ) ?? null
  );
}

export default function CallbacksOverview() {
  return (
    <>
      <ContinuityHeader
        title="Callbacks"
        intro="PAS is watching the promises your brokerage made. Callback promises become operational objects, not memory — tracked, owned, and recoverable."
      />

      <CommitmentWatch />

      <ul className={continuity.recordList} aria-label="Callbacks">
        {DEMO_CALLBACKS.map((callback) => (
          <CallbackCard
            key={callback.id}
            callback={callback}
            evidenceIds={evidenceForCallback(callback.id)}
            relatedProposal={proposalForCallback(callback.id)}
          />
        ))}
      </ul>

      <p className={continuity.disclaimer}>
        This is demo/rehearsal data. PAS has not changed live customer behavior.
      </p>
    </>
  );
}
