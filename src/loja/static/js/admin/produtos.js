const successMessage = document.querySelector('.success')
const errorMessage = document.querySelector('.error')
const pageMessage = document.querySelector('.message-page')
const addProdutoPopUp = document.querySelector('.addproduto-popup')
const addProdutoMessage = document.querySelector('.criar-produto')
const editProdutoMessage = document.querySelector('.editar-produto')
const editProdutoPopUp = document.querySelector('.editproduto-popup')

function abrirAddProduto() {
    addProdutoPopUp.style.visibility = 'visible'
    addProdutoPopUp.style.opacity = '1'
}

function fecharAddProduto() {
    addProdutoPopUp.style.visibility = 'hidden'
    addProdutoPopUp.style.opacity = '0'
}

function abrirEditProduto(id) {
    document.getElementById(`editproduto-popup-${id}`).style.visibility = 'visible';
    document.getElementById(`editproduto-popup-${id}`).style.opacity = '1';
}

function fecharEditProduto(id) {
    document.getElementById(`editproduto-popup-${id}`).style.visibility = 'hidden';
    document.getElementById(`editproduto-popup-${id}`).style.opacity = '0';
}

function abrirExcluirProduto(id) {
    document.getElementById(`excluirproduto-popup-${id}`).style.visibility = 'visible';
    document.getElementById(`excluirproduto-popup-${id}`).style.opacity = '1';
}

function fecharExcluirProduto(id) {
    document.getElementById(`excluirproduto-popup-${id}`).style.visibility = 'hidden';
    document.getElementById(`excluirproduto-popup-${id}`).style.opacity = '0';
}

if (pageMessage) {
    setTimeout(function() {
        window.location.href = produtosUrl
    }, 1000)
} else if (addProdutoMessage) {
    addProdutoPopUp.style.visibility = 'visible'
    addProdutoPopUp.style.opacity = '1'
    if (successMessage) {
        setTimeout(function() {
            window.location.href = produtosUrl
        }, 1000)
    } else if (errorMessage) {
        setTimeout(function() {
            window.location.href = produtosUrl
        }, 2000)
    }
} else if (editProdutoMessage) {
    editProdutoPopUp.style.visibility = 'visible'
    editProdutoPopUp.style.opacity = '1'
    if (successMessage) {
        setTimeout(function() {
            window.location.href = produtosUrl
        }, 1000)
    } else if (errorMessage) {
        setTimeout(function() {
            window.location.href = produtosUrl
        }, 2000)
    }
}