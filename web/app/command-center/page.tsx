import type { Metadata } from "next";
import CommandCenterOverview from "@/components/modules/command-center/CommandCenterOverview";
import styles from "./page.module.css";

export const metadata: Metadata = {
  title: "Command Center",
};

export default function CommandCenterPage() {
  return (
    <main className={styles.page} aria-label="Command Center">
      <CommandCenterOverview />
    </main>
  );
}
