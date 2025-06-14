export interface IconProps {
    icon: React.ReactNode;
    href: string;
}

export interface NavLinkProps extends IconProps {
    name: string;
}

export const pageList: Record<string, string> = {
    '/promocoes': 'Promoções',
    '/perfil': 'Meu Perfil',
}

export interface MenuContextType {
  menuOpen: boolean
  setMenuOpen: (open: boolean) => void
}