import Link from 'next/link';

import { IoMdCart } from "react-icons/io";
import { FaBell } from "react-icons/fa";

import Icon from '@/components/Icon';

const Topbar = ({page}: {page: string}) => {
    return (
        <div className="flex items-center justify-between">
            <h1 className="text-3xl font-bold">{page}</h1>
            <div className='flex items-center gap-4'>
                <div className="flex items-center gap-2">
                    <Icon icon={<FaBell size={20}/>} href="/notificacoes" />
                    <Icon icon={<IoMdCart size={20}/>} href="/carrinho" />
                </div>
                <div className='flex items-center gap-2'>
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