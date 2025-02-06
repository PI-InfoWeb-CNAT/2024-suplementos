const successMessage = document.querySelector('.success')
const errorMessage = document.querySelector('.error')
const dadosMessage = document.querySelector('.message-dados')
const redefinirSenhaMessage = document.querySelector('.message-redefinirsenha')
const redefinirSenhaPopUp = document.querySelector('.redefinirsenha-popup')
const excluirPopUp = document.querySelector('.excluirconta-popup')

function abrirRedefinirSenha() {
    redefinirSenhaPopUp.style.visibility = 'visible'
    redefinirSenhaPopUp.style.opacity = '1'
}

function fecharRedefinirSenha() {
    redefinirSenhaPopUp.style.visibility = 'hidden'
    redefinirSenhaPopUp.style.opacity = '0'
}

function abrirExcluir() {
    excluirPopUp.style.visibility = 'visible'
    excluirPopUp.style.opacity = '1'
}

function fecharExcluir() {
    excluirPopUp.style.visibility = 'hidden'
    excluirPopUp.style.opacity = '0'
}

if (dadosMessage) {
    setTimeout(function() {
        window.location.href = perfilUrl
    }, 1000)
} else if (redefinirSenhaMessage) {
    redefinirSenhaPopUp.style.visibility = 'visible'
    redefinirSenhaPopUp.style.opacity = '1'
    setTimeout(function() {
        window.location.href = perfilUrl
    }, 1000)
}