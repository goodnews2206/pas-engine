/*
 * CallbackCard — one callback promise as an operational record (flagship).
 * Static, demo-only. Resolves owner, evidence, and any related recovery
 * proposal from the model.
 */

import type {
  Callback,
  CallbackStatus,
  ActionProposal,
} from "@/lib/demo/operational";
import OperationalRecordCard from "@/components/modules/continuity/OperationalRecordCard";
import OwnershipBadge from "@/components/modules/continuity/OwnershipBadge";
import RiskChip from "@/components/modules/continuity/RiskChip";
import EvidenceMiniList from "@/components/modules/continuity/EvidenceMiniList";
import {
  railColorForSeverity,
  formatIso,
} from "@/components/modules/continuity/severity";
import continuity from "@/components/modules/continuity/continuity.module.css";
import styles from "./callbacks.module.css";

const STATUS_LABELS: Record<CallbackStatus, string> = {
  promised: "Promised",
  due_soon: "Due soon",
  overdue: "Overdue",
  kept: "Kept",
  missed: "Missed",
  recovered: "Recovered",
};

interface Props {
  callback: Callback;
  evidenceIds: string[];
  relatedProposal: ActionProposal | null;
}

export default function CallbackCard({
  callback,
  evidenceIds,
  relatedProposal,
}: Props) {
  return (
    <OperationalRecordCard
      recordId={callback.id}
      title={`Callback · Demo Lead ${callback.leadId}`}
      railColor={railColorForSeverity(callback.riskLevel)}
      chips={
        <>
          <span className={continuity.statusChip}>
            {STATUS_LABELS[callback.status]}
          </span>
          <RiskChip severity={callback.riskLevel} />
        </>
      }
      footer={<OwnershipBadge agentId={callback.ownerId} />}
    >
      <dl className={continuity.fields}>
        <div className={continuity.field}>
          <dt className={continuity.fieldLabel}>Promised</dt>
          <dd className={continuity.fieldValue}>{formatIso(callback.promisedAt)}</dd>
        </div>
        <div className={continuity.field}>
          <dt className={continuity.fieldLabel}>Due</dt>
          <dd className={continuity.fieldValue}>{formatIso(callback.dueAt)}</dd>
        </div>
        <div className={continuity.field}>
          <dt className={continuity.fieldLabel}>Lead</dt>
          <dd className={continuity.fieldValue}>Demo Lead {callback.leadId}</dd>
        </div>
        <div className={continuity.field}>
          <dt className={continuity.fieldLabel}>Source call</dt>
          <dd className={continuity.fieldValue}>{callback.sourceCallId}</dd>
        </div>
      </dl>

      <p className={continuity.notePas}>
        PAS proposed recovery: {callback.proposedRecovery}
      </p>

      {relatedProposal && (
        <p className={styles.cardProposal}>
          Recovery proposal {relatedProposal.id}: {relatedProposal.title} ·
          demo-only
        </p>
      )}

      <div>
        <p className={continuity.sectionLabel}>Receipt</p>
        <EvidenceMiniList evidenceIds={evidenceIds} />
      </div>
    </OperationalRecordCard>
  );
}
