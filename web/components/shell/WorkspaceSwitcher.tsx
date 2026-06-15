/*
 * WorkspaceSwitcher — Sidebar workspace shell (PAS301B). Static RSC, demo-only.
 *
 * Makes the ACTIVE workspace and the current role/hat unmistakable, and previews
 * the PAS301 "one identity, many workspaces" model. This is NOT real switching:
 * the list is read from the build-time DEMO_SESSION and every control is inert.
 * No auth, no backend, no persistence, no membership enforcement — those land in
 * later checkpoints.
 *
 * Doctrine (PAS301 §3): a person owns their identity and professional self; a
 * workspace governs the business records created within it.
 */

import { DEMO_SESSION, type DemoWorkspaceType } from "@/lib/session/demoSession";
import styles from "./WorkspaceSwitcher.module.css";

const TYPE_LABELS: Record<DemoWorkspaceType, string> = {
  personal: "Personal",
  team: "Team",
  brokerage: "Brokerage",
  orvn: "ORVN",
};

export default function WorkspaceSwitcher() {
  const { workspaces, activeWorkspaceId } = DEMO_SESSION;
  const active =
    workspaces.find((w) => w.id === activeWorkspaceId) ?? workspaces[0];
  const others = workspaces.filter((w) => w.id !== active.id);

  return (
    <section className={styles.switcher} aria-label="Workspace">
      <p className={styles.eyebrow}>One identity · many workspaces</p>

      {/* Active workspace card — the unmistakable "where am I acting" control */}
      <div className={styles.activeCard}>
        <div className={styles.activeTop}>
          <span className={styles.activeName}>{active.name}</span>
          <span className={styles.typeBadge}>{TYPE_LABELS[active.type]}</span>
        </div>
        <span className={styles.hat}>Acting as {active.role}</span>
        <p className={styles.activeSummary}>{active.summary}</p>
      </div>

      {/* Other workspaces — inert preview of future switching */}
      <div className={styles.listBlock}>
        <p className={styles.listLabel}>Your other workspaces</p>
        <ul className={styles.list}>
          {others.map((w) => (
            <li key={w.id}>
              <button
                type="button"
                className={styles.wsItem}
                disabled
                aria-label={`${w.name} — ${TYPE_LABELS[w.type]} · switching coming later`}
              >
                <span className={styles.wsItemName}>{w.name}</span>
                <span className={styles.typeBadgeMuted}>
                  {TYPE_LABELS[w.type]}
                </span>
              </button>
            </li>
          ))}
        </ul>
        <p className={styles.note}>Switching workspaces comes later.</p>
      </div>

      {/* My obligations — inert cross-workspace placeholder (PAS301 §7) */}
      <div className={styles.obligations}>
        <p className={styles.listLabel}>My obligations</p>
        <p className={styles.obligationsNote}>
          Will show your own follow-ups and responsibilities across workspaces —
          only ever your own, never another workspace&rsquo;s records. Coming
          later.
        </p>
      </div>
    </section>
  );
}
