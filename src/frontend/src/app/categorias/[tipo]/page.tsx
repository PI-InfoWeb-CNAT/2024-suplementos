const Categorias = ({ params }: { params: { tipo: string } }) => {
  const { tipo } = params;

  return (
    <p>{tipo}</p>
  )
}

export default Categorias;