import { Metadata } from "next";
import Link from "next/link";

import { FaMagnifyingGlass, FaBottleWater, FaShirt } from "react-icons/fa6";
import { BsFillLightningChargeFill } from "react-icons/bs";
import { GiKnifeFork } from "react-icons/gi";

import { Carousel, CarouselContent, CarouselItem } from "@/components/ui/carousel";
import { CategoryProps } from "@/types/index";

export const metadata: Metadata = {
  title: "PowerUP - Página Principal", 
};

const Category = ({href, icon, name, isEven}: CategoryProps) => {
  return (
    <Link href={`/categorias/${href}`} className={`flex justify-center items-center gap-5 w-full menu:w-[45%] nt-lg:w-[48%] dt:w-1/5 h-15 menu:h-20 text-base tb:text-xl text-white p-4 rounded-lg shadow-[0_0_10px_0_rgba(0,0,0,0.6)] ${isEven ? 'bg-dark-grey' : 'bg-dark-green'}`}>
      {icon}
      {name}
    </Link>
  )
}

export default function Home() {
  return (
    <main className="flex flex-col mb-sm:gap-10 gap-7">
      <section>
        <form action="">
          <div className="relative">
            <input type="text" placeholder="Encontre o seu produto" className="bg-dark-grey text-white text-sm mb-lg:text-base w-full mb-lg:px-15 px-12 py-3 outline-none rounded-lg"/>
            <button className="cursor-pointer absolute left-0 mb-lg:top-[25%] top-[28%] ml-3 text-light-green mb-lg:text-2xl text-xl">
              <FaMagnifyingGlass />
            </button>
          </div>
        </form>
      </section>
      <section className="slides">
        <Carousel>
          <CarouselContent>
            <CarouselItem>
              <img
                src="/carrossel/imagem1_carrossel.webp"
                alt="Imagem 1"
                className="w-full object-cover nt-sm:rounded-[30px] mb:rounded-[15px] rounded-[10px]"
              />
            </CarouselItem>
            <CarouselItem>
              <img
                src="/carrossel/imagem2_carrossel.webp"
                alt="Imagem 2"
                className="w-full object-cover nt-sm:rounded-[30px] mb:rounded-[15px] rounded-[10px]"
              />
            </CarouselItem>
            <CarouselItem>
              <img
                src="/carrossel/imagem3_carrossel.webp"
                alt="Imagem 3"
                className="w-full object-cover nt-sm:rounded-[30px] mb:rounded-[15px] rounded-[10px]"
              />
            </CarouselItem>
            <CarouselItem>
              <img
                src="/carrossel/imagem4_carrossel.webp"
                alt="Imagem 4"
                className="w-full object-cover nt-sm:rounded-[30px] mb:rounded-[15px] rounded-[10px]"
              />
            </CarouselItem>
          </CarouselContent>
        </Carousel>
      </section>
      <section className="flex flex-col gap-5">
        <h2 className="h2">Categorias</h2>
        <div className="flex justify-between items-center flex-wrap gap-y-5">
          <Category href="acessorios" icon={<FaBottleWater className="text-light-green text-3xl tb:text-4xl" />} name="Acessórios" isEven={true} />
          <Category href="alimentos" icon={<GiKnifeFork className="text-black text-3xl tb:text-4xl" />} name="Alimentos" isEven={false} />
          <Category href="roupas" icon={<FaShirt className="text-light-green text-3xl tb:text-4xl" />} name="Roupas" isEven={true} />
          <Category href="suplementos" icon={<BsFillLightningChargeFill className="text-black text-3xl tb:text-4xl" />} name="Suplementos" isEven={false} />
        </div>
      </section>
    </main>
  );
}
