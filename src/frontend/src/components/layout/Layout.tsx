'use client';

import { usePathname } from 'next/navigation';

import { pageList } from '@/types/index';
import Sidebar from "./Sidebar";
import Topbar from "./Topbar";

const Layout = ({ children }: { children: React.ReactNode }) => {
  const pathname = usePathname();
  const pageName = pageList[pathname] || 'Página Inicial';

  return (
    <div>
        <div className="flex gap-15 mx-48 my-16">
            <Sidebar />
            <div className="flex-1 flex flex-col">
                <Topbar page={pageName} />
                <main className="p-6 flex-1">
                    {children}
                </main>
            </div>
        </div>
    </div>
  )
}

export default Layout;