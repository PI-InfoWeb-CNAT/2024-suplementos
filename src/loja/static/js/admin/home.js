const successMessage = document.querySelector('.success')
const errorMessage = document.querySelector('.error')
const pageMessage = document.querySelector('.page-lotes')
const editLoteMessage = document.querySelector('.editar-lote')
const editLotePopUp = document.querySelector('.editlote-popup')
const excluirLotePopUp = document.querySelector('.excluirlote-popup')

function abrirEditLote(id) {
    document.getElementById(`editlote-popup-${id}`).style.visibility = 'visible';
    document.getElementById(`editlote-popup-${id}`).style.opacity = '1';
}

function fecharEditLote(id) {
    document.getElementById(`editlote-popup-${id}`).style.visibility = 'hidden';
    document.getElementById(`editlote-popup-${id}`).style.opacity = '0';
}

function abrirExcluirLote(id) {
    document.getElementById(`excluirlote-popup-${id}`).style.visibility = 'visible';
    document.getElementById(`excluirlote-popup-${id}`).style.opacity = '1';
}

function fecharExcluirLote(id) {
    document.getElementById(`excluirlote-popup-${id}`).style.visibility = 'hidden';
    document.getElementById(`excluirlote-popup-${id}`).style.opacity = '0';
}

if (pageMessage) {
    setTimeout(function() {
        window.location.href = homeUrl
    }, 1000)
}

if (editLoteMessage) {
    editLotePopUp.style.visibility = 'visible'
    editLotePopUp.style.opacity = '1'
    if (successMessage) {
        setTimeout(function() {
            window.location.href = homeUrl
        }, 1000)
    } else if (errorMessage) {
        setTimeout(function() {
            window.location.href = homeUrl
        }, 2000)
    }
}