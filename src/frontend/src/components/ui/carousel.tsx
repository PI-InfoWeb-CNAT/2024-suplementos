"use client"

import React from "react"
import useEmblaCarousel from "embla-carousel-react"

type CarouselProps = {
  children: React.ReactNode
}

function Carousel({ children }: CarouselProps) {
  const [emblaRef, emblaApi] = useEmblaCarousel()
  const [selectedIndex, setSelectedIndex] = React.useState(0)
  const [scrollSnaps, setScrollSnaps] = React.useState<number[]>([])
  const intervalRef = React.useRef<NodeJS.Timeout | null>(null)

  React.useEffect(() => {
    if (!emblaApi) return

    setScrollSnaps(emblaApi.scrollSnapList())

    const onSelect = () => {
      setSelectedIndex(emblaApi.selectedScrollSnap())
    }

    emblaApi.on("select", onSelect)
    onSelect()
  }, [emblaApi])

  // Função que configura o autoplay (intervalo)
  const startAutoplay = React.useCallback(() => {
    if (!emblaApi) return
    // Limpa o intervalo anterior se existir
    if (intervalRef.current) clearInterval(intervalRef.current)

    intervalRef.current = setInterval(() => {
      if (!emblaApi) return

      if (emblaApi.canScrollNext()) {
        emblaApi.scrollNext()
      } else {
        emblaApi.scrollTo(0)
      }
    }, 4000)
  }, [emblaApi])

  // Inicia autoplay quando emblaApi estiver pronto
  React.useEffect(() => {
    startAutoplay()
    return () => {
      if (intervalRef.current) clearInterval(intervalRef.current)
    }
  }, [startAutoplay])

  const scrollTo = (index: number) => {
    if (!emblaApi) return
    emblaApi.scrollTo(index)
    // Reseta o autoplay ao clicar na bolinha
    startAutoplay()
  }

  return (
    <div className="relative w-full">
      <div className="overflow-hidden" ref={emblaRef}>
        <div className="flex">{children}</div>
      </div>

      {/* Dots */}
      <div className="flex justify-center gap-2 mt-4">
        {scrollSnaps.map((_, index) => {
          const isActive = selectedIndex === index
          return (
            <button
              key={index}
              onClick={() => scrollTo(index)}
              className={`transition-all rounded-full h-5 ${
                isActive
                  ? "w-12 bg-dark-green"
                  : "w-5 bg-[#6C6A6A] hover:bg-dark-grey cursor-pointer"
              }`}
            />
          )
        })}
      </div>
    </div>
  )
}

function CarouselContent({ children }: { children: React.ReactNode }) {
  return (
    <>
      {React.Children.map(children, (child) => (
        <div className="min-w-full">{child}</div>
      ))}
    </>
  )
}

function CarouselItem({
  children,
  className = "",
}: {
  children: React.ReactNode
  className?: string
}) {
  return (
    <div
      className={`min-w-0 shrink-0 grow-0 basis-full ${className}`}
      role="group"
      aria-roledescription="slide"
    >
      {children}
    </div>
  )
}

export { Carousel, CarouselContent, CarouselItem }
