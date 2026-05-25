import type { NextConfig } from "next";

const config: NextConfig = {
  // /web is the frontend root; Railway hosts the Python backend separately.
  // No rewrites to the backend yet — API wiring lands in a later step once
  // the Vercel domain is known and CORS is updated in app/main.py.
};

export default config;
