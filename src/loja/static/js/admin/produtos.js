const successMessage = document.querySelector('.success')
const errorMessage = document.querySelector('.error')
const pageMessage = document.querySelector('.message-page')
const editProdutoPopUp = document.querySelector('.editproduto-popup')

function abrirEditProduto(id) {
    document.getElementById(`editproduto-popup-${id}`).style.visibility = 'visible';
    document.getElementById(`editproduto-popup-${id}`).style.opacity = '1';
}

function fecharEditProduto(id) {
    document.getElementById(`editproduto-popup-${id}`).style.visibility = 'hidden';
    document.getElementById(`editproduto-popup-${id}`).style.opacity = '0';
}

if (pageMessage) {
    setTimeout(function() {
        window.location.href = produtosUrl
    }, 1000)
}