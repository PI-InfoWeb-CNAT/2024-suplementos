import { ProductProps } from "@/types/products";

const ProductCard = ({ product }: {product: ProductProps}) => {
    return (
        <a className="flex flex-col w-[220px] bg-white">
            <div className="">
                <img src={product.imagem} alt={`Imagem do produto ${product.nome}`} className="rounded-3xl"/>
            </div>
            <div className="rounded-b-3xl shadow-lg px-5 pt-12 pb-5 -mt-7 space-y-3">
                <h5 className="text-xl font-semibold">{product.nome}</h5>
                <div className="flex justify-between items-center">
                    <div>
                        {product.porcentagem_desconto > 0 && 
                            <p className="text-sm line-through">{product.preco} R$</p>
                        }
                        <p className="text-xl font-semibold">{product.preco_calculado.toFixed(2)} R$</p>
                    </div>
                    {product.porcentagem_desconto > 0 &&
                        <div className="bg-dark-grey text-light-green px-2 py-1 rounded-md">
                            {product.porcentagem_desconto}% OFF
                        </div>
                    }
                </div>
            </div>
            <div>

            </div>
        </a>
    );
}

export default ProductCard;