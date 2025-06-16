'use client';

import { FaMagnifyingGlass } from "react-icons/fa6";
import { Carousel, CarouselContent, CarouselItem } from "@/components/ui/carousel";

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
      <section>
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
    </main>
  );
}
