/*
 * EvidenceMiniList — resolves evidenceIds to demo evidence receipts.
 * Static, demo-only. Links point to in-app demo routes (no network).
 */

import { DEMO_EVIDENCE } from "@/lib/demo/operational";
import styles from "./continuity.module.css";

const EVIDENCE_BY_ID = Object.fromEntries(DEMO_EVIDENCE.map((e) => [e.id, e]));

interface Props {
  evidenceIds: string[];
}

export default function EvidenceMiniList({ evidenceIds }: Props) {
  const items = evidenceIds
    .map((id) => EVIDENCE_BY_ID[id])
    .filter((e): e is (typeof DEMO_EVIDENCE)[number] => Boolean(e));

  if (items.length === 0) {
    return <p className={styles.evidenceEmpty}>No evidence linked yet.</p>;
  }

  return (
    <ul className={styles.evidence}>
      {items.map((evidence) => (
        <li key={evidence.id} className={styles.evidenceItem}>
          <a className={styles.evidenceLink} href={evidence.link}>
            {evidence.id}
          </a>
          <span className={styles.evidenceText}>{evidence.summary}</span>
        </li>
      ))}
    </ul>
  );
}
