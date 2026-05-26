"use client";

/*
 * NavList — client component for session-aware, pathname-aware navigation.
 *
 * Display-only scaffold. Real security belongs to the backend/auth layer.
 * DEMO_SESSION is a static constant; swap for a real server session in the
 * auth step (Frontend Foundation Plan §14 Step 5 auth phase).
 */

import Link from "next/link";
import { usePathname } from "next/navigation";
import { DEMO_SESSION } from "@/lib/session/demoSession";
import { getNavGroupsForSession } from "@/lib/session/permissions";
import styles from "./Sidebar.module.css";

export default function NavList() {
  const pathname = usePathname();
  const groups = getNavGroupsForSession(DEMO_SESSION);

  return (
    <>
      {groups.map((group) => (
        <div key={group.family} className={styles.group}>
          <span className={styles.groupLabel} aria-hidden="true">
            {group.family}
          </span>
          <ul className={styles.items} role="list">
            {group.routes.map((route) => {
              const isActive =
                pathname === route.href ||
                pathname.startsWith(route.href + "/");
              return (
                <li key={route.id} role="listitem">
                  <Link
                    href={route.href}
                    className={
                      isActive
                        ? `${styles.item} ${styles.active}`
                        : styles.item
                    }
                    aria-current={isActive ? "page" : undefined}
                    title={route.description}
                  >
                    {route.label}
                  </Link>
                </li>
              );
            })}
          </ul>
        </div>
      ))}
    </>
  );
}
