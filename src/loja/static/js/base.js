const ajudaPopUp = document.querySelector('.ajuda-popup')

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