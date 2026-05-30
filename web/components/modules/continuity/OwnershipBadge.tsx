/*
 * OwnershipBadge — resolves an agentId to its demo name. Static, demo-only.
 * Falls back to the id (clearly demo) if the agent is not in the model.
 */

import { DEMO_AGENTS } from "@/lib/demo/operational";
import styles from "./continuity.module.css";

const AGENT_NAMES: Record<string, string> = Object.fromEntries(
  DEMO_AGENTS.map((a) => [a.id, a.name]),
);

interface Props {
  agentId: string;
}

export default function OwnershipBadge({ agentId }: Props) {
  const name = AGENT_NAMES[agentId] ?? agentId;
  return (
    <span className={styles.ownership} title={`Owner: ${name}`}>
      {name}
    </span>
  );
}
