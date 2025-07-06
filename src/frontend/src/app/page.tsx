import { Metadata } from 'next'
import HomeClient from './HomeClient'

export const metadata: Metadata = {
  title: "PowerUP - Página Inicial", 
};

export default function Home() {
  return <HomeClient />
}
