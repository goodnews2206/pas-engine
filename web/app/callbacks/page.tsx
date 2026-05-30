import type { Metadata } from "next";
import CallbacksOverview from "@/components/modules/callbacks/CallbacksOverview";
import styles from "./page.module.css";

export const metadata: Metadata = { title: "Callbacks" };

export default function CallbacksPage() {
  return (
    <main className={styles.page} aria-label="Callbacks">
      <CallbacksOverview />
    </main>
  );
}
