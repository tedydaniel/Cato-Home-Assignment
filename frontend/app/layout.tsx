import type { Metadata } from "next";
import "./globals.css";
import { AppProvider } from "./providers";
export const metadata: Metadata = { title: "Cato AI Support Engineer" };
export default function RootLayout({ children }: Readonly<{children: React.ReactNode}>) { return <html lang="en"><body><AppProvider>{children}</AppProvider></body></html>; }
