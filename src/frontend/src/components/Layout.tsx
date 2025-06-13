import Sidebar from "./Sidebar"
import Topbar from "./Topbar"

const Layout = ({ children }: { children: React.ReactNode }) => {
  return (
    <div>
        <div className="flex gap-12 mx-48 my-16">
            <Sidebar />
            <div className="flex-1 flex flex-col">
                <Topbar />
                <main className="p-6 flex-1">
                    {children}
                </main>
            </div>
        </div>
    </div>
  )
}

export default Layout;