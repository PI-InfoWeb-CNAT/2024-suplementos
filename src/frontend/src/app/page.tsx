'use client';

import { FaMagnifyingGlass } from "react-icons/fa6";
import { Carousel, CarouselContent, CarouselItem } from "@/components/ui/carousel";
import Autoplay from "embla-carousel-autoplay";

export default function Home() {
  return (
    <main className="flex flex-col gap-10">
      <section>
        <form action="">
          <div className="relative">
            <input type="text" placeholder="Encontre o seu produto" className="bg-dark-grey text-white w-full px-15 py-3 outline-none rounded-xl"/>
            <button className="cursor-pointer absolute left-0 top-3 ml-3 text-light-green text-2xl">
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
                className="w-full object-cover rounded-[30px]"
              />
            </CarouselItem>
            <CarouselItem>
              <img
                src="/carrossel/imagem2_carrossel.webp"
                alt="Imagem 2"
                className="w-full object-cover rounded-[30px]"
              />
            </CarouselItem>
            <CarouselItem>
              <img
                src="/carrossel/imagem3_carrossel.webp"
                alt="Imagem 3"
                className="w-full object-cover rounded-[30px]"
              />
            </CarouselItem>
            <CarouselItem>
              <img
                src="/carrossel/imagem4_carrossel.webp"
                alt="Imagem 4"
                className="w-full object-cover rounded-[30px]"
              />
            </CarouselItem>
          </CarouselContent>
        </Carousel>
      </section>
    </main>
  );
}
