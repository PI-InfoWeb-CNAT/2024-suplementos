import Link from 'next/link';

import { IconProps } from '@/types/index';

const Icon = ({icon, href}: IconProps) => {
    return (
        <Link href={href} className='bg-dark-grey text-light-green flex justify-center items-center w-max p-2 rounded-full hover:scale-110 transition-all duration-[200ms]'>
            {icon}
        </Link>
    )
}

export default Icon;