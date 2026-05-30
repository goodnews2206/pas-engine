import { apiGet } from "./client";

/** Matches the existing backend GET /health response. */
export interface HealthResponse {
  status: string;
  system: string;
}

/**
 * Calls GET /health on the PAS API.
 * Returns null when in demo mode (IS_DEMO_MODE = true).
 * Throws PasApiError or PasConnectionError on failure.
 */
export async function fetchHealth(): Promise<HealthResponse | null> {
  return apiGet<HealthResponse>("/health");
}
