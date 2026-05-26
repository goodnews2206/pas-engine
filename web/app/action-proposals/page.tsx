import type { Metadata } from "next";
import ModuleSkeleton from "@/components/modules/ModuleSkeleton";
import { ROUTES_BY_ID } from "@/lib/navigation/routes";
import { MODULE_EMPTY_STATES } from "@/lib/demo/moduleEmptyStates";

export const metadata: Metadata = { title: "Action Proposals" };

export default function ActionProposalsPage() {
  return (
    <ModuleSkeleton
      route={ROUTES_BY_ID["action-proposals"]}
      emptyState={MODULE_EMPTY_STATES["action-proposals"]}
    />
  );
}
