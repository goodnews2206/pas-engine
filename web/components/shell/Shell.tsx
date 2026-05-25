import DemoBanner from "./DemoBanner";
import Sidebar from "./Sidebar";
import TopBar from "./TopBar";
import TenantStrip from "./TenantStrip";
import Composer from "./Composer";
import styles from "./Shell.module.css";

export default function Shell({ children }: { children: React.ReactNode }) {
  return (
    <div className={styles.root}>
      <DemoBanner />
      <div className={styles.frame}>
        <Sidebar />
        <div className={styles.main}>
          <TopBar />
          <TenantStrip />
          <div className={styles.content}>{children}</div>
          <Composer />
        </div>
      </div>
    </div>
  );
}
