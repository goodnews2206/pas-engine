import type { Metadata } from "next";
import SettingsOverview from "@/components/modules/settings/SettingsOverview";
import styles from "./page.module.css";

export const metadata: Metadata = { title: "Settings" };

export default function SettingsPage() {
  return (
    <main className={styles.page} aria-label="Settings">
      <SettingsOverview />
    </main>
  );
}
