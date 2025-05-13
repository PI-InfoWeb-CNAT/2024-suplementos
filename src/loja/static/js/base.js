const ajudaPopUp = document.querySelector('.ajuda-popup')

function abrir() {
    ajudaPopUp.style.visibility = 'visible'
    ajudaPopUp.style.opacity = '1'
}

function fechar() {
    ajudaPopUp.style.visibility = 'hidden'
    ajudaPopUp.style.opacity = '0'
}