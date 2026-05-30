/*
 * AgentCard — one agent's operational snapshot. Static RSC, demo-only.
 * Severity is never colour alone: coverage uses a left rail + a labelled chip.
 */

import type { Agent, CoverageStatus, Role } from "@/lib/demo/operational";
import styles from "./AgentCard.module.css";

const ROLE_LABELS: Record<Role, string> = {
  broker_owner: "Broker Owner",
  admin: "Admin / Ops",
  team_lead: "Team Lead",
  agent: "Agent",
  viewer: "Viewer",
  orvn_internal_admin: "ORVN Internal Admin",
};

const COVERAGE: Record<
  CoverageStatus,
  { label: string; chip: string; rail: string }
> = {
  covered: { label: "Available", chip: styles.chipFyi, rail: "var(--signal-fyi)" },
  stretched: {
    label: "Stretched",
    chip: styles.chipAttention,
    rail: "var(--signal-attention)",
  },
  gap: { label: "Coverage gap", chip: styles.chipUrgent, rail: "var(--signal-urgent)" },
};

function minutes(ms: number): string {
  return `${Math.round(ms / 60_000)} min`;
}

interface AgentCardProps {
  agent: Agent;
  overdueCallbacks: number;
  callsLogged: number;
}

export default function AgentCard({
  agent,
  overdueCallbacks,
  callsLogged,
}: AgentCardProps) {
  const coverage = COVERAGE[agent.coverageStatus];

  return (
    <article className={styles.card}>
      <div className={styles.rail} style={{ background: coverage.rail }} aria-hidden="true" />
      <div className={styles.body}>
        <div className={styles.headerRow}>
          <h3 className={styles.name}>{agent.name}</h3>
          <span className={styles.demoPill}>Simulated</span>
        </div>

        <div className={styles.badges}>
          <span className={styles.roleBadge}>{ROLE_LABELS[agent.role]}</span>
          <span className={`${styles.chip} ${coverage.chip}`}>{coverage.label}</span>
        </div>

        <dl className={styles.stats}>
          <div className={styles.stat}>
            <dt className={styles.statLabel}>Active leads</dt>
            <dd className={styles.statValue}>{agent.activeLeads}</dd>
          </div>
          <div className={styles.stat}>
            <dt className={styles.statLabel}>Callbacks owned</dt>
            <dd className={styles.statValue}>{agent.callbacksOwned}</dd>
          </div>
          <div className={styles.stat}>
            <dt className={styles.statLabel}>Overdue</dt>
            <dd
              className={
                overdueCallbacks > 0
                  ? `${styles.statValue} ${styles.statValueAlert}`
                  : styles.statValue
              }
            >
              {overdueCallbacks}
            </dd>
          </div>
          <div className={styles.stat}>
            <dt className={styles.statLabel}>Calls logged</dt>
            <dd className={styles.statValue}>{callsLogged}</dd>
          </div>
          <div className={styles.stat}>
            <dt className={styles.statLabel}>Avg first response</dt>
            <dd className={styles.statValue}>{minutes(agent.responseSpeedMs)}</dd>
          </div>
        </dl>

        <p className={styles.pasNote}>
          {agent.coachingFlags.length > 0
            ? `PAS is watching: ${agent.coachingFlags.join(", ").replace(/_/g, " ")}.`
            : "PAS has no open concerns for this agent right now."}
        </p>

        <div className={styles.footer}>
          <span className={styles.permissionBadge}>
            {ROLE_LABELS[agent.permissionsRole]} · display-only
          </span>
        </div>
      </div>
    </article>
  );
}
