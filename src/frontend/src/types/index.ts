export const pageList: Record<string, string> = {
    '/promocoes': 'Promoções',
    '/perfil': 'Meu Perfil',
}

export interface IconProps {
    icon: React.ReactNode;
    href: string;
}

export interface NavLinkProps extends IconProps {
    name: string;
}

export interface CategoryProps {
    icon: React.ReactNode;
    name: string;
    isEven: boolean;
}

export interface MenuContextType {
    menuOpen: boolean
    setMenuOpen: (open: boolean) => void
}