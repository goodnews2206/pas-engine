"use client";

/*
 * ConnectionStatus — live API boundary indicator.
 * Replaces the static "Demo / rehearsal" chip in TopBar.
 * Demo mode: no network call. Connected/Offline: single health check on mount.
 * No retries. No polling. No hidden network behavior.
 */

import { useEffect, useState } from "react";
import { IS_DEMO_MODE } from "@/lib/api/config";
import { fetchHealth } from "@/lib/api/health";
import styles from "./ConnectionStatus.module.css";

type ConnectionState = "demo" | "connecting" | "connected" | "offline";

const LABELS: Record<ConnectionState, string> = {
  demo: "Demo mode",
  connecting: "Connecting…",
  connected: "API connected",
  offline: "Offline",
};

export default function ConnectionStatus() {
  const [state, setState] = useState<ConnectionState>(
    IS_DEMO_MODE ? "demo" : "connecting",
  );

  useEffect(() => {
    if (IS_DEMO_MODE) return;

    let cancelled = false;

    fetchHealth()
      .then((result) => {
        if (!cancelled) setState(result ? "connected" : "offline");
      })
      .catch(() => {
        if (!cancelled) setState("offline");
      });

    return () => {
      cancelled = true;
    };
  }, []);

  const label = LABELS[state];

  return (
    <span
      className={`${styles.chip} ${styles[state]}`}
      aria-label={`PAS connection status: ${label}`}
      role="status"
    >
      <span className={styles.dot} aria-hidden="true" />
      {label}
    </span>
  );
}
