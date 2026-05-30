"use client";

/*
 * RoomComposerDemo — local-only operational note input. Demo-only.
 * On submit it appends locally (via onSend) and shows a confirmation.
 * No network, no persistence (state resets on refresh).
 */

import { useState } from "react";
import { NOTIFICATION_REPLY_CONFIRMATION } from "@/lib/demo/operational";
import styles from "./PasRoomOverview.module.css";

interface Props {
  onSend: (text: string) => void;
}

export default function RoomComposerDemo({ onSend }: Props) {
  const [text, setText] = useState("");
  const [confirmed, setConfirmed] = useState(false);

  function handleSubmit() {
    const trimmed = text.trim();
    if (!trimmed) return;
    onSend(trimmed);
    setText("");
    setConfirmed(true);
  }

  return (
    <div className={styles.composer}>
      <label htmlFor="room-composer" className={styles.composerHint}>
        Ask PAS or leave an operational note
      </label>
      <textarea
        id="room-composer"
        className={styles.composerInput}
        placeholder="Ask PAS or leave an operational note…"
        value={text}
        onChange={(e) => {
          setText(e.target.value);
          if (confirmed) setConfirmed(false);
        }}
        aria-label="Ask PAS or leave an operational note"
      />
      <div className={styles.composerRow}>
        <span className={styles.composerHint}>
          Demo only — nothing is sent or saved.
        </span>
        <button
          type="button"
          className={styles.sendBtn}
          onClick={handleSubmit}
          disabled={text.trim().length === 0}
        >
          Add note
        </button>
      </div>
      {confirmed && (
        <p className={styles.confirmation} role="status">
          {NOTIFICATION_REPLY_CONFIRMATION}
        </p>
      )}
    </div>
  );
}
