const produtoMessage = document.querySelector('.message-produto')
const successMessage = document.querySelector('.success')
const errorMessage = document.querySelector('.error')

if (produtoMessage) {
    if (successMessage) {
        setTimeout(function() {
            window.location.href = carrinhoUrl
        }, 1000)
    } else if (errorMessage) {
        setTimeout(function() {
            window.location.href = "/produto/" + produtoId + "/"
        }, 1500)
    }
}