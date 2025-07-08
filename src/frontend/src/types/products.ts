export interface ProductProps {
  id: number;
  nome: string;
  preco: number;
  descricao: string;
  imagem: string; 
  porcentagem_desconto: number;
  categoria: string;
  preco_calculado: number; 
}

export interface ProductContextType {
  produtos: ProductProps[];
  loading: boolean;
}