"use client";

/*
 * NavList — client component for role-shaped, pathname-aware navigation.
 *
 * DISPLAY-ONLY role shaping. Not a security boundary.
 * Real role resolution + permission gates land in Step 5 (auth).
 * DEMO_ROLE is a static constant; swap it in Step 5 once session context exists.
 */

import Link from "next/link";
import { usePathname } from "next/navigation";
import { DEMO_ROLE, getNavGroupsForRole } from "@/lib/navigation/routes";
import styles from "./Sidebar.module.css";

export default function NavList() {
  const pathname = usePathname();
  const groups = getNavGroupsForRole(DEMO_ROLE);

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
