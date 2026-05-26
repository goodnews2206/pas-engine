import type { Metadata } from "next";
import ModuleSkeleton from "@/components/modules/ModuleSkeleton";
import { ROUTES_BY_ID } from "@/lib/navigation/routes";
import { MODULE_EMPTY_STATES } from "@/lib/demo/moduleEmptyStates";

export const metadata: Metadata = { title: "Integrations" };

export default function IntegrationsPage() {
  return (
    <ModuleSkeleton
      route={ROUTES_BY_ID["integrations"]}
      emptyState={MODULE_EMPTY_STATES["integrations"]}
    />
  );
}
