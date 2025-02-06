const AddCartaoPopUp = document.querySelector('.novocartao-popup')
const editCartaoPopUp = document.querySelector('.editcartao-popup')
const novoCartaoMessage = document.querySelector('.message-novocartao')
const editCartaoMessage = document.querySelector('.message-editcartao')
const pageMessage = document.querySelector('.message-pageCarteira')
const successMessage = document.querySelector('.success')
const errorMessage = document.querySelector('.error')

function abrirAddCartao() {
    AddCartaoPopUp.style.visibility = 'visible'
    AddCartaoPopUp.style.opacity = '1'
}

function fecharAddCartao() {
    AddCartaoPopUp.style.visibility = 'hidden'
    AddCartaoPopUp.style.opacity = '0'
}

function abrirEditCartao(id) {
    document.getElementById(`editcartao-popup-${id}`).style.visibility = 'visible';
    document.getElementById(`editcartao-popup-${id}`).style.opacity = '1';
}

function fecharEditCartao(id) {
    document.getElementById(`editcartao-popup-${id}`).style.visibility = 'hidden';
    document.getElementById(`editcartao-popup-${id}`).style.opacity = '0';
}

if (pageMessage) {
    setTimeout(function() {
        window.location.href = minhaCarteiraUrl
    }, 1000)
}

if (novoCartaoMessage) {
    AddCartaoPopUp.style.visibility = 'visible'
    AddCartaoPopUp.style.opacity = '1'
    if (errorMessage) {
        setTimeout(function() {
            window.location.href = minhaCarteiraUrl
        }, 2000)
    }
    if (successMessage) {
        setTimeout(function() {
            window.location.href = minhaCarteiraUrl
        }, 1000)
    }
}

if (editCartaoMessage) {
    editCartaoPopUp.style.visibility = 'visible'
    editCartaoPopUp.style.opacity = '1'
    if (errorMessage) {
        setTimeout(function() {
            window.location.href = minhaCarteiraUrl
        }, 2000)
    }
    if (successMessage) {
        setTimeout(function() {
            window.location.href = minhaCarteiraUrl
        }, 1000)
    }
}