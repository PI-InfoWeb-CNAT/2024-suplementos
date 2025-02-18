const successMessage = document.querySelector('.success')
const errorMessage = document.querySelector('.error')
const pageMessage = document.querySelector('.page-devolucoes')
const editDevolucaoMessage = document.querySelector('.editar-devolucao')
const editDevolucaoPopUp = document.querySelector('.editdevolucao-popup')

function abrirDetalhesDevolucao(id) {
    document.getElementById(`detalhesdevolucao-popup-${id}`).style.visibility = 'visible';
    document.getElementById(`detalhesdevolucao-popup-${id}`).style.opacity = '1';
}

function fecharDetalhesDevolucao(id) {
    document.getElementById(`detalhesdevolucao-popup-${id}`).style.visibility = 'hidden';
    document.getElementById(`detalhesdevolucao-popup-${id}`).style.opacity = '0';
}

function abrirEditDevolucao(id) {
    document.getElementById(`editdevolucao-popup-${id}`).style.visibility = 'visible';
    document.getElementById(`editdevolucao-popup-${id}`).style.opacity = '1';
}

function fecharEditDevolucao(id) {
    document.getElementById(`editdevolucao-popup-${id}`).style.visibility = 'hidden';
    document.getElementById(`editdevolucao-popup-${id}`).style.opacity = '0';
}

function abrirExcluirDevolucao(id) {
    document.getElementById(`excluirdevolucao-popup-${id}`).style.visibility = 'visible';
    document.getElementById(`excluirdevolucao-popup-${id}`).style.opacity = '1';
}

function fecharExcluirDevolucao(id) {
    document.getElementById(`excluirdevolucao-popup-${id}`).style.visibility = 'hidden';
    document.getElementById(`excluirdevolucao-popup-${id}`).style.opacity = '0';
}

if (pageMessage) {
    setTimeout(function() {
        window.location.href = devolucoesUrl
    }, 1000)
}

if (editDevolucaoMessage) {
    editDevolucaoPopUp.style.visibility = 'visible'
    editDevolucaoPopUp.style.opacity = '1'
    if (successMessage) {
        setTimeout(function() {
            window.location.href = devolucoesUrl
        }, 1000)
    } else if (errorMessage) {
        setTimeout(function() {
            window.location.href = devolucoesUrl
        }, 2000)
    }
}