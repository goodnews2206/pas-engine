/*
 * AgentsOverview — operational demo surface for the Agents (People) module.
 * Static RSC. Consumes the typed demo data model (PR A). No network, no auth,
 * no mutations. Every figure is rehearsal data.
 *
 * Answers: who is available · who owns follow-up · where coverage is weak ·
 * which agents need attention · what PAS recommends watching.
 */

import {
  DEMO_AGENTS,
  DEMO_USERS,
  DEMO_CALLBACKS,
  DEMO_CALLS,
} from "@/lib/demo/operational";
import AgentCard from "./AgentCard";
import AgentCoveragePanel from "./AgentCoveragePanel";
import AgentSignalsPanel from "./AgentSignalsPanel";
import styles from "./AgentsOverview.module.css";

export default function AgentsOverview() {
  // Derived, demo-only relations across the model.
  const overdueByAgent: Record<string, number> = {};
  for (const cb of DEMO_CALLBACKS) {
    if (cb.status === "overdue") {
      overdueByAgent[cb.ownerId] = (overdueByAgent[cb.ownerId] ?? 0) + 1;
    }
  }

  const callsByAgent: Record<string, number> = {};
  for (const call of DEMO_CALLS) {
    callsByAgent[call.agentId] = (callsByAgent[call.agentId] ?? 0) + 1;
  }

  return (
    <>
      <header className={styles.header}>
        <div className={styles.headerTop}>
          <h1 className={styles.title}>Agents</h1>
          <span className={styles.demoPill}>Simulated</span>
        </div>
        <p className={styles.subtitle}>
          Northwind Realty (DEMO) · {DEMO_AGENTS.length} agents ·{" "}
          {DEMO_USERS.length} managers
        </p>
        <p className={styles.lead}>
          PAS is watching agent coverage against callback promises and active
          lead ownership.
        </p>
        <p className={styles.rehearsalNote}>
          Rehearsal mode — these figures are simulated.
        </p>
      </header>

      <AgentCoveragePanel />

      <section className={styles.grid} aria-label="Agent roster">
        {DEMO_AGENTS.map((agent) => (
          <AgentCard
            key={agent.id}
            agent={agent}
            overdueCallbacks={overdueByAgent[agent.id] ?? 0}
            callsLogged={callsByAgent[agent.id] ?? 0}
          />
        ))}
      </section>

      <AgentSignalsPanel />

      <p className={styles.disclaimer}>
        This is demo/rehearsal data. PAS has not changed live customer behavior.
      </p>
    </>
  );
}
