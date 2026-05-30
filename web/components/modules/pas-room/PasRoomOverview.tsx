/*
 * PasRoomOverview — the PAS Room surface. Static RSC shell wrapping a client
 * feed (local composer) + RSC object-thread panel. Demo-only.
 *
 * Answers: what the team is discussing operationally · which messages tie to
 * work objects · what PAS said · what decisions are recorded · which objects
 * have active threads · how communication becomes company memory.
 *
 * Communication is attached to work — company memory, not a chat channel.
 */

import {
  DEMO_THREADS,
  DEMO_USERS,
  DEMO_AGENTS,
} from "@/lib/demo/operational";
import RoomMessageFeed from "./RoomMessageFeed";
import ObjectThreadPanel from "./ObjectThreadPanel";
import styles from "./PasRoomOverview.module.css";

export default function PasRoomOverview() {
  const authorNames: Record<string, string> = {
    PAS: "PAS",
    ...Object.fromEntries(DEMO_USERS.map((u) => [u.id, u.name])),
    ...Object.fromEntries(DEMO_AGENTS.map((a) => [a.id, a.name])),
  };

  const roomThread = DEMO_THREADS.find((t) => t.objectType === "room");
  const objectThreads = DEMO_THREADS.filter((t) => t.objectType !== "room");

  return (
    <>
      <header className={styles.header}>
        <div className={styles.headerTop}>
          <h1 className={styles.title}>PAS Room</h1>
          <span className={styles.demoPill}>Simulated</span>
        </div>
        <p className={styles.intro}>
          PAS Room keeps brokerage decisions attached to the work they affect.
          This is not a chat channel — it is operating memory.
        </p>
        <p className={styles.subIntro}>
          Messages shown here are demo/rehearsal data.
        </p>
        <p className={styles.rehearsalNote}>
          Rehearsal mode — nothing here is sent, delivered, or saved.
        </p>
      </header>

      <div className={styles.layout}>
        <RoomMessageFeed
          seedMessages={roomThread ? [...roomThread.messages] : []}
          authorNames={authorNames}
        />
        <ObjectThreadPanel threads={[...objectThreads]} authorNames={authorNames} />
      </div>

      <p className={styles.disclaimer}>
        This is demo/rehearsal data. PAS has not changed live customer behavior.
      </p>
    </>
  );
}
