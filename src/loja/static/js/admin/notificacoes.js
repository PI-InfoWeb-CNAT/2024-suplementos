const successMessage = document.querySelector('.success')
const errorMessage = document.querySelector('.error')
const pageMessage = document.querySelector('.page-notificacoesadmin')
const addNotificacaoMessage = document.querySelector('.criar-notificacao')
const editNotificacaoMessage = document.querySelector('.editar-notificacao')
const addNotificacaoPopUp = document.querySelector('.addnotificacao-popup')
const editNotificacaoPopUp = document.querySelector('.editnotificacao-popup')

function abrirAddNotificacao() {
    addNotificacaoPopUp.style.visibility = 'visible'
    addNotificacaoPopUp.style.opacity = '1'
}

function fecharAddNotificacao() {
    addNotificacaoPopUp.style.visibility = 'hidden'
    addNotificacaoPopUp.style.opacity = '0'
}

function abrirEditNotificacao(id) {
    document.getElementById(`editnotificacao-popup-${id}`).style.visibility = 'visible';
    document.getElementById(`editnotificacao-popup-${id}`).style.opacity = '1';
}

function fecharEditNotificacao(id) {
    document.getElementById(`editnotificacao-popup-${id}`).style.visibility = 'hidden';
    document.getElementById(`editnotificacao-popup-${id}`).style.opacity = '0';
}

function abrirExcluirNotificacao(id) {
    document.getElementById(`excluirnotificacao-popup-${id}`).style.visibility = 'visible';
    document.getElementById(`excluirnotificacao-popup-${id}`).style.opacity = '1';
}

function fecharExcluirNotificacao(id) {
    document.getElementById(`excluirnotificacao-popup-${id}`).style.visibility = 'hidden';
    document.getElementById(`excluirnotificacao-popup-${id}`).style.opacity = '0';
}

if (pageMessage) {
    setTimeout(function() {
        window.location.href = notificacoesUrl
    }, 1000)
} else if (addNotificacaoMessage) {
    addNotificacaoPopUp.style.visibility = 'visible'
    addNotificacaoPopUp.style.opacity = '1'
    if (successMessage) {
        setTimeout(function() {
            window.location.href = notificacoesUrl
        }, 1000)
    } else if (errorMessage) {
        setTimeout(function() {
            window.location.href = notificacoesUrl
        }, 2000)
    }
} else if (editNotificacaoMessage) {
    editNotificacaoPopUp.style.visibility = 'visible'
    editNotificacaoPopUp.style.opacity = '1'
    if (successMessage) {
        setTimeout(function() {
            window.location.href = notificacoesUrl
        }, 1000)
    } else if (errorMessage) {
        setTimeout(function() {
            window.location.href = notificacoesUrl
        }, 2000)
    }
}