/*
 * LeadCard — one demo lead as an operational record. Static, demo-only.
 * Name is a clearly-fictional id label (no real-sounding client names).
 */

import type { Lead, LeadStage } from "@/lib/demo/operational";
import OperationalRecordCard from "@/components/modules/continuity/OperationalRecordCard";
import OwnershipBadge from "@/components/modules/continuity/OwnershipBadge";
import RiskChip from "@/components/modules/continuity/RiskChip";
import {
  railColorForSeverity,
  formatIso,
} from "@/components/modules/continuity/severity";
import styles from "@/components/modules/continuity/continuity.module.css";

const STAGE_LABELS: Record<LeadStage, string> = {
  new: "New",
  contacted: "Contacted",
  qualified: "Qualified",
  nurturing: "Nurturing",
  appointment_set: "Appointment set",
  won: "Won",
  lost: "Lost",
};

interface Props {
  lead: Lead;
  callbackCount: number;
  callCount: number;
}

export default function LeadCard({ lead, callbackCount, callCount }: Props) {
  return (
    <OperationalRecordCard
      recordId={lead.id}
      title={`Demo Lead ${lead.id}`}
      railColor={railColorForSeverity(lead.riskLevel)}
      chips={
        <>
          <RiskChip severity={lead.riskLevel} />
          <span className={styles.statusChip}>{STAGE_LABELS[lead.stage]}</span>
        </>
      }
      footer={<OwnershipBadge agentId={lead.ownerId} />}
    >
      <dl className={styles.fields}>
        <div className={styles.field}>
          <dt className={styles.fieldLabel}>Source</dt>
          <dd className={styles.fieldValue}>{lead.source}</dd>
        </div>
        <div className={styles.field}>
          <dt className={styles.fieldLabel}>Last touch</dt>
          <dd className={styles.fieldValue}>{formatIso(lead.lastTouch)}</dd>
        </div>
        <div className={styles.field}>
          <dt className={styles.fieldLabel}>Callbacks</dt>
          <dd className={styles.fieldValue}>{callbackCount}</dd>
        </div>
        <div className={styles.field}>
          <dt className={styles.fieldLabel}>Calls</dt>
          <dd className={styles.fieldValue}>{callCount}</dd>
        </div>
      </dl>
      <p className={styles.note}>
        <strong>Next:</strong> {lead.nextAction}
      </p>
      <p className={styles.notePas}>PAS: {lead.pasNote}</p>
    </OperationalRecordCard>
  );
}
