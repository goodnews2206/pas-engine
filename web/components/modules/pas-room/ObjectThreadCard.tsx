/*
 * ObjectThreadCard — a discussion welded to one work object. Static,
 * presentational, demo-only.
 */

import styles from "./PasRoomOverview.module.css";

export interface ObjectThreadView {
  id: string;
  typeLabel: string;
  title: string;
  lastMessage: string;
  participants: number;
  statusLabel: string;
  evidenceCount: number;
}

interface Props {
  thread: ObjectThreadView;
}

export default function ObjectThreadCard({ thread }: Props) {
  return (
    <li className={styles.thread}>
      <div className={styles.threadTop}>
        <span className={styles.threadType}>{thread.typeLabel}</span>
        <span className={styles.threadStatus}>{thread.statusLabel}</span>
      </div>
      <p className={styles.threadTitle}>{thread.title}</p>
      <p className={styles.threadLast}>{thread.lastMessage}</p>
      <div className={styles.threadMeta}>
        <span className={styles.threadMetaItem}>
          {thread.participants} participant
          {thread.participants === 1 ? "" : "s"}
        </span>
        <span className={styles.threadMetaItem}>
          {thread.evidenceCount} receipt
          {thread.evidenceCount === 1 ? "" : "s"}
        </span>
      </div>
    </li>
  );
}
