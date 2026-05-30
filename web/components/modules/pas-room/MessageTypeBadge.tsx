/*
 * MessageTypeBadge — typed message vocabulary as a labelled chip.
 * Meaning is carried by the label (never colour alone). Static, demo-only.
 */

import type { MessageType } from "@/lib/demo/operational";
import styles from "./PasRoomOverview.module.css";

const TYPE_META: Record<MessageType, { label: string; cls: string }> = {
  human: { label: "Note", cls: "" },
  pas: { label: "PAS", cls: styles.typePas },
  approval: { label: "Approval", cls: styles.typeApproval },
  assignment: { label: "Assignment", cls: "" },
  evidence_reference: { label: "Evidence", cls: "" },
  decision_record: { label: "Decision", cls: styles.typeDecision },
};

interface Props {
  type: MessageType;
}

export default function MessageTypeBadge({ type }: Props) {
  const meta = TYPE_META[type];
  return (
    <span className={`${styles.typeBadge} ${meta.cls}`}>{meta.label}</span>
  );
}
