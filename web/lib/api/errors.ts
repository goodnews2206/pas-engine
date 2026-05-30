/** Raised when the PAS API responds with a non-2xx status. */
export class PasApiError extends Error {
  constructor(
    public readonly status: number,
    message: string,
  ) {
    super(message);
    this.name = "PasApiError";
  }
}

/** Raised when the PAS API cannot be reached (network failure or timeout). */
export class PasConnectionError extends Error {
  constructor(message = "Could not reach PAS API") {
    super(message);
    this.name = "PasConnectionError";
  }
}

export function isPasApiError(e: unknown): e is PasApiError {
  return e instanceof PasApiError;
}

export function isPasConnectionError(e: unknown): e is PasConnectionError {
  return e instanceof PasConnectionError;
}
