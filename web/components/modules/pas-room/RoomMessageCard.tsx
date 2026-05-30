/*
 * RoomMessageCard — one message in the operating room feed. Static,
 * presentational, demo-only. Takes a normalized view model so it renders
 * both seed messages and local demo appends.
 */

import type { MessageType } from "@/lib/demo/operational";
import EvidenceMiniList from "@/components/modules/continuity/EvidenceMiniList";
import MessageTypeBadge from "./MessageTypeBadge";
import styles from "./PasRoomOverview.module.css";

export interface RoomMessageView {
  id: string;
  author: string;
  type: MessageType;
  body: string;
  evidenceIds: string[];
  tsLabel: string;
}

interface Props {
  message: RoomMessageView;
}

export default function RoomMessageCard({ message }: Props) {
  return (
    <li className={styles.message}>
      <div className={styles.messageTop}>
        <span className={styles.author}>{message.author}</span>
        <MessageTypeBadge type={message.type} />
        <span className={styles.ts}>{message.tsLabel}</span>
      </div>
      <p className={styles.body}>{message.body}</p>
      {message.evidenceIds.length > 0 && (
        <div>
          <p className={styles.evidenceLabel}>Receipt</p>
          <EvidenceMiniList evidenceIds={message.evidenceIds} />
        </div>
      )}
    </li>
  );
}
