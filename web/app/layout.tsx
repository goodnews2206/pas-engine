import type { Metadata } from "next";
import { Inter, JetBrains_Mono } from "next/font/google";
import Shell from "../components/shell/Shell";
import "./globals.css";

const inter = Inter({
  variable: "--font-inter",
  subsets: ["latin"],
  display: "swap",
});

const jetbrainsMono = JetBrains_Mono({
  variable: "--font-jetbrains-mono",
  subsets: ["latin"],
  display: "swap",
});

export const metadata: Metadata = {
  title: {
    default: "PAS — ORVN",
    template: "%s — PAS",
  },
  description:
    "Making your company queryable, adaptive, and operationally intelligent.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={`${inter.variable} ${jetbrainsMono.variable}`}>
        <Shell>{children}</Shell>
      </body>
    </html>
  );
}
