import Link from 'next/link';
import Image from "next/image";

import { IoMenu } from "react-icons/io5";
import { IoMdCart } from "react-icons/io";

import Icon from '@/components/Icon';
import { useMenu } from '@/context/MenuContext';

const Topbar = ({page}: {page: string}) => {
    const { setMenuOpen } = useMenu();

    return (
        <div className="flex items-center justify-between">
            <h1 className="hidden nt-sm:block text-3xl font-bold">{page}</h1> 
            <button className='nt-sm:hidden' onClick={() => setMenuOpen(true)}>
                <Icon icon={<IoMenu className='text-[18px] tb:text-[22px]' />} href="/" />
            </button>
            <div className='nt-sm:hidden relative w-[130px] h-[30px] mb-lg:w-[150px] mb-lg:h-[35px] tb:w-[170px] tb:h-[40px]'>
                <Image src="/Logo-preta-longa.webp" fill alt="Logo preta da PowerUP" />
            </div>
            <div className='flex items-center gap-2'>
                <Icon icon={<IoMdCart className='text-[18px] tb:text-[22px]' />} href="/carrinho" />
                {/* DESKTOP */}
                <div className='hidden nt-sm:flex items-center gap-2'>
                    <Link href="/login" className=" bg-dark-grey py-2 px-4 text-white text-base rounded-tl-[10px] rounded-br-[10px] hover:text-light-green transition-color-slow">
                        Entrar
                    </Link>
                    <Link href="/cadastro" className=" bg-dark-grey py-2 px-4 text-white text-base rounded-tl-[10px] rounded-br-[10px] hover:text-light-green transition-color-slow">
                        Cadastrar
                    </Link>
                </div>
            </div>
        </div>
    );
}

export default Topbar;