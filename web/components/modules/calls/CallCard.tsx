/*
 * CallCard — one demo call record. Static, demo-only. No live calling.
 * Resolves owner + evidence from the model.
 */

import type { Call, CallOutcome, Sentiment } from "@/lib/demo/operational";
import OperationalRecordCard from "@/components/modules/continuity/OperationalRecordCard";
import OwnershipBadge from "@/components/modules/continuity/OwnershipBadge";
import EvidenceMiniList from "@/components/modules/continuity/EvidenceMiniList";
import { formatIso } from "@/components/modules/continuity/severity";
import styles from "@/components/modules/continuity/continuity.module.css";

const OUTCOME_LABELS: Record<CallOutcome, string> = {
  connected: "Connected",
  voicemail: "Voicemail",
  no_answer: "No answer",
  scheduled_callback: "Scheduled callback",
  appointment_set: "Appointment set",
};

const SENTIMENT_LABELS: Record<Sentiment, string> = {
  positive: "Positive",
  neutral: "Neutral",
  hesitant: "Hesitant",
  negative: "Negative",
};

interface Props {
  call: Call;
  createdCallback: boolean;
}

export default function CallCard({ call, createdCallback }: Props) {
  return (
    <OperationalRecordCard
      recordId={call.id}
      title={`Call · Demo Lead ${call.leadId}`}
      railColor="var(--border-strong)"
      chips={
        <>
          <span className={styles.statusChip}>{OUTCOME_LABELS[call.outcome]}</span>
          <span className={styles.statusChip}>
            {SENTIMENT_LABELS[call.sentiment]}
          </span>
          {createdCallback && (
            <span className={styles.statusChip}>Created a callback</span>
          )}
        </>
      }
      footer={<OwnershipBadge agentId={call.agentId} />}
    >
      <dl className={styles.fields}>
        <div className={styles.field}>
          <dt className={styles.fieldLabel}>Lead</dt>
          <dd className={styles.fieldValue}>Demo Lead {call.leadId}</dd>
        </div>
        <div className={styles.field}>
          <dt className={styles.fieldLabel}>Occurred</dt>
          <dd className={styles.fieldValue}>{formatIso(call.occurredAt)}</dd>
        </div>
      </dl>
      <p className={styles.note}>
        <strong>Objection / intent:</strong> {call.objection}
      </p>
      <p className={styles.notePas}>“{call.transcriptPreview}”</p>
      <p className={styles.note}>
        <strong>Next:</strong> {call.nextAction}
      </p>
      <div>
        <p className={styles.sectionLabel}>Evidence PAS captured</p>
        <EvidenceMiniList evidenceIds={call.evidenceIds} />
      </div>
    </OperationalRecordCard>
  );
}
