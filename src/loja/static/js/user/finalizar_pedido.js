const successMessage = document.querySelector('.success')
const errorMessage = document.querySelector('.error')
const pedidoMessage = document.querySelector('.page-pedido')

if (pedidoMessage) {
    if (successMessage) {
        setTimeout(function() {
            window.location.href = meusPedidosUrl
        }, 1000)
    } else if (errorMessage) {
        setTimeout(function() {
            window.location.href = finalizarPedidoUrl
        }, 2000)
    }
}