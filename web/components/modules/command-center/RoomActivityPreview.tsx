/*
 * RoomActivityPreview — what the team and PAS have already discussed. Static
 * RSC, demo-only. Shows the latest operating-room messages. Links to /pas-room.
 */

import Link from "next/link";
import {
  DEMO_THREADS,
  DEMO_USERS,
  DEMO_AGENTS,
} from "@/lib/demo/operational";
import styles from "./CommandCenterOverview.module.css";

const AUTHOR_NAMES: Record<string, string> = {
  PAS: "PAS",
  ...Object.fromEntries(DEMO_USERS.map((u) => [u.id, u.name])),
  ...Object.fromEntries(DEMO_AGENTS.map((a) => [a.id, a.name])),
};

export default function RoomActivityPreview() {
  const room = DEMO_THREADS.find((t) => t.objectType === "room");
  const recent = room ? room.messages.slice(-2) : [];

  return (
    <section className={styles.snapshot} aria-label="Team discussion">
      <div className={styles.snapshotHeader}>
        <h2 className={styles.snapshotTitle}>What the team is discussing</h2>
        <Link href="/pas-room" className={styles.moduleLink}>
          PAS Room →
        </Link>
      </div>
      <p className={styles.snapshotLead}>
        Decisions stay attached to the work they affect — operating memory, not
        chat noise.
      </p>
      <div>
        {recent.map((message) => (
          <div key={message.id} className={styles.roomMsg}>
            <span className={styles.roomAuthor}>
              {AUTHOR_NAMES[message.authorId] ?? message.authorId}
            </span>
            <span className={styles.roomBody}>{message.body}</span>
          </div>
        ))}
      </div>
    </section>
  );
}
