import type { Metadata } from "next";
import AgentsOverview from "@/components/modules/agents/AgentsOverview";
import styles from "./page.module.css";

export const metadata: Metadata = {
  title: "Agents",
};

export default function AgentsPage() {
  return (
    <main className={styles.page} aria-label="Agents">
      <AgentsOverview />
    </main>
  );
}
