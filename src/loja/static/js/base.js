const ajuda = document.querySelector('.ajuda')
const ajudaPopUp = document.querySelector('.ajuda-popup')

const AlturaPagina = document.documentElement.scrollHeight || document.body.scrollHeight
ajuda.style.marginTop = `${AlturaPagina - 717}px`

function MudarCoracao(button) {
    const icon = button.querySelector('i');
    if (icon.classList.contains('bi-heart')) {
        icon.classList.remove('bi-heart');
        icon.classList.add('bi-heart-fill');
    } else {
        icon.classList.remove('bi-heart-fill');
        icon.classList.add('bi-heart');
    }
}

function abrir() {
    ajudaPopUp.style.visibility = 'visible'
    ajudaPopUp.style.opacity = '1'
}

function fechar() {
    ajudaPopUp.style.visibility = 'hidden'
    ajudaPopUp.style.opacity = '0'
}