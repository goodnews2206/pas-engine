/*
 * CallsOverview — operational demo for /calls. Static RSC, demo-only.
 * Answers: what happened on recent calls · what PAS learned · which calls
 * created follow-up commitments. Consumes DEMO_CALLS + DEMO_CALLBACKS.
 */

import { DEMO_CALLS, DEMO_CALLBACKS } from "@/lib/demo/operational";
import ContinuityHeader from "@/components/modules/continuity/ContinuityHeader";
import ContinuityMetricStrip from "@/components/modules/continuity/ContinuityMetricStrip";
import CallCard from "./CallCard";
import styles from "@/components/modules/continuity/continuity.module.css";

export default function CallsOverview() {
  const callbackSourceCallIds = new Set(
    DEMO_CALLBACKS.map((cb) => cb.sourceCallId),
  );

  const connected = DEMO_CALLS.filter((c) => c.outcome === "connected").length;
  const createdFollowUp = DEMO_CALLS.filter((c) =>
    callbackSourceCallIds.has(c.id),
  ).length;

  return (
    <>
      <ContinuityHeader
        title="Calls"
        intro="Recent calls with their outcome, the objection or intent PAS heard, and the commitments they created."
      />

      <ContinuityMetricStrip
        ariaLabel="Call summary"
        metrics={[
          { label: "Calls logged", value: DEMO_CALLS.length },
          { label: "Connected", value: connected, tone: "fyi" },
          {
            label: "Created follow-up",
            value: createdFollowUp,
            tone: createdFollowUp > 0 ? "attention" : "neutral",
          },
        ]}
      />

      <ul className={styles.recordList} aria-label="Calls">
        {DEMO_CALLS.map((call) => (
          <CallCard
            key={call.id}
            call={call}
            createdCallback={callbackSourceCallIds.has(call.id)}
          />
        ))}
      </ul>

      <p className={styles.disclaimer}>
        This is demo/rehearsal data. PAS has not changed live customer behavior.
      </p>
    </>
  );
}
