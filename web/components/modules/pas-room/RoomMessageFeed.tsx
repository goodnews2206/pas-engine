"use client";

/*
 * RoomMessageFeed — the operating room feed + local demo composer. Client
 * island: holds locally-appended demo messages (in-memory only, no network,
 * no persistence). Seed messages come from the demo model.
 */

import { useState } from "react";
import type { RoomMessage } from "@/lib/demo/operational";
import RoomMessageCard, { type RoomMessageView } from "./RoomMessageCard";
import RoomComposerDemo from "./RoomComposerDemo";
import styles from "./PasRoomOverview.module.css";

interface Props {
  seedMessages: RoomMessage[];
  authorNames: Record<string, string>;
}

export default function RoomMessageFeed({ seedMessages, authorNames }: Props) {
  const [appended, setAppended] = useState<RoomMessageView[]>([]);

  const seedViews: RoomMessageView[] = seedMessages.map((m) => ({
    id: m.id,
    author: authorNames[m.authorId] ?? m.authorId,
    type: m.type,
    body: m.body,
    evidenceIds: [...m.evidenceIds],
    tsLabel: formatTs(m.ts),
  }));

  const messages = [...seedViews, ...appended];

  function handleSend(text: string) {
    setAppended((prev) => [
      ...prev,
      {
        id: `LOCAL-${prev.length + 1}`,
        author: "You (demo)",
        type: "human",
        body: text,
        evidenceIds: [],
        tsLabel: "Just now · demo",
      },
    ]);
  }

  return (
    <section className={styles.region} aria-label="Operating room feed">
      <div className={styles.regionHeader}>
        <h2 className={styles.regionTitle}>Operating room</h2>
        <p className={styles.regionDesc}>
          A calm, low-volume record of what PAS noticed, what was decided, and
          what the team coordinated.
        </p>
      </div>

      <ul className={styles.feed}>
        {messages.map((message) => (
          <RoomMessageCard key={message.id} message={message} />
        ))}
      </ul>

      <RoomComposerDemo onSend={handleSend} />
    </section>
  );
}

/** Deterministic ISO → label (no Date object). */
function formatTs(iso: string): string {
  const [date, rest] = iso.replace("Z", "").split("T");
  const time = rest ? rest.slice(0, 5) : "";
  return time ? `${date} · ${time} UTC` : date;
}
