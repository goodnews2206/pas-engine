import type { Metadata } from "next";
import CallsOverview from "@/components/modules/calls/CallsOverview";
import styles from "./page.module.css";

export const metadata: Metadata = { title: "Calls" };

export default function CallsPage() {
  return (
    <main className={styles.page} aria-label="Calls">
      <CallsOverview />
    </main>
  );
}
