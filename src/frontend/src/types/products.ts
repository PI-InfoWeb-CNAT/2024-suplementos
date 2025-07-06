export interface Produto {
  id: number;
  nome: string;
  preco: number;
  descricao: string;
  imagem: string; 
  porcentagem_desconto: number;
  categoria: string;
}

export interface ProdutosContextType {
  produtos: Produto[];
  loading: boolean;
}