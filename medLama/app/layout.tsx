// Root layout for MedLama frontend (Next.js)
import './globals.css';
import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import ThemeProviderClient from './theme-provider-client';

const inter = Inter({ subsets: ['latin'] });

// Metadata for SEO and browser
export const metadata: Metadata = {
  title: 'MedLama - AI Health Assistant',
  description: 'AI-powered health triage and symptom analysis',
};

// Main layout component
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body suppressHydrationWarning={true} className={inter.className}>
        <ThemeProviderClient>
          {children}
        </ThemeProviderClient>
      </body>
    </html>
  );
}