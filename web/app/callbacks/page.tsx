import type { Metadata } from "next";
import ModuleSkeleton from "@/components/modules/ModuleSkeleton";
import { ROUTES_BY_ID } from "@/lib/navigation/routes";

export const metadata: Metadata = { title: "Callbacks" };

export default function CallbacksPage() {
  return <ModuleSkeleton route={ROUTES_BY_ID["callbacks"]} />;
}
