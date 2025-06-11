import type { Metadata } from "next";
import { Bai_Jamjuree } from "next/font/google";
import "./globals.css";

const baiJamjuree = Bai_Jamjuree({
  variable: "--font-bai-jamjuree",
  subsets: ["latin"],
  weight: ["400", "600", "700"],
});

export const metadata: Metadata = {
  title: "PowerUP",
  description: "E-commerce de uma loja de suplementos",
  keywords: ["ecommerce", "suplementos", "loja"],
  openGraph: {
    title: "E-commerce de uma loja de suplementos",
    description: "Veja os melhores produtos do mercado",
    siteName: "PowerUP",
    type: "website",
  },
};

export default function RootLayout({ children }: 
  Readonly<{children: React.ReactNode;}>
) {
  return (
    <html lang="en">
      <head>
        <link rel="icon" href="/favicons/favicon-light.ico" media="(prefers-color-scheme: dark)"/>
        <link rel="icon" href="/favicons/favicon-dark.ico" media="(prefers-color-scheme: light)"/>
      </head>
      <body className={`${baiJamjuree.variable} antialiased`}>
        {children}
      </body>
    </html>
  );
}