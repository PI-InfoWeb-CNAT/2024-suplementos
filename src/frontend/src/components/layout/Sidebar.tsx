'use client';

import Link from 'next/link';
import Image from "next/image";
import { usePathname } from 'next/navigation';

import { NavLinkProps } from '@/types/index';
import logo from '../../../public/Logo-preta-longa.webp';
import { useMenu } from '@/context/MenuContext'

import { IoHomeSharp } from "react-icons/io5";
import { BsFillLightningChargeFill, BsBasket3Fill } from "react-icons/bs";
import { FaTrophy } from "react-icons/fa";
import { FaHeart } from "react-icons/fa6";
import { BiSolidUser } from "react-icons/bi";
import { IoMdClose } from "react-icons/io";

const NavLink = ({href, icon, name}: NavLinkProps) => {
    const pathname = usePathname()
    const isActive = pathname === href

    return (
        <li>
            <Link href={href} 
            className={`flex items-center gap-3 text-lg font-semibold pl-3
            ${isActive ? 'text-dark-green border-l-2 border-dark-green transition-border-fast' : 'text-dark-grey hover:text-dark-green transition-color-slow'}`}
            >
                {icon}
                {name}
            </Link>
        </li>
    );
}

const Sidebar = () => {
    const { menuOpen, setMenuOpen } = useMenu()

    return (
        <>
            {/* Mobile Sidebar */}
            {menuOpen && (
                <aside className="nt-sm:hidden fixed top-0 left-0 z-3 w-2/5 h-full bg-white flex flex-col gap-15 px-10 py-15">
                    <button onClick={() => setMenuOpen(false)} className="absolute top-5 right-5 cursor-pointer">
                        <IoMdClose size={40} className="text-light-blue hover:text-white" />
                    </button>
                    <nav>
                        <ul className="flex flex-col gap-6">
                            <NavLink href="/" icon={<IoHomeSharp size={24} />} name="Página Inicial" />
                            <NavLink href="/promocoes" icon={<BsFillLightningChargeFill size={24} />} name="Promoções" />
                            <NavLink href="/mais-vendidos" icon={<FaTrophy size={24} />} name="Mais Vendidos" />
                            <NavLink href="/meus-pedidos" icon={<BsBasket3Fill size={24} />} name="Meus Pedidos" />
                            <NavLink href="/meus-favoritos" icon={<FaHeart size={24} />} name="Meus Favoritos" />
                            <NavLink href="/perfil" icon={<BiSolidUser size={24} />} name="Meu Perfil" />
                        </ul>
                    </nav>
                </aside>
            )}

            {/* Desktop Sidebar */}
            <aside className="hidden nt-sm:flex flex-col gap-15 w-max h-screen">
                <Link href="/">
                    <Image src={logo} width={170} height={60} alt="Logo preta da PowerUP" />
                </Link>
                <nav>
                    <ul className="flex flex-col gap-6">
                        <NavLink href="/" icon={<IoHomeSharp size={24} />} name="Página Inicial" />
                        <NavLink href="/promocoes" icon={<BsFillLightningChargeFill size={24} />} name="Promoções" />
                        <NavLink href="/mais-vendidos" icon={<FaTrophy size={24} />} name="Mais Vendidos" />
                        <NavLink href="/meus-pedidos" icon={<BsBasket3Fill size={24} />} name="Meus Pedidos" />
                        <NavLink href="/meus-favoritos" icon={<FaHeart size={24} />} name="Meus Favoritos" />
                        <NavLink href="/perfil" icon={<BiSolidUser size={24} />} name="Meu Perfil" />
                    </ul>
                </nav>
            </aside>
        </>
    )
}

export default Sidebar;