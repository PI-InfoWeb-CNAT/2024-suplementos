const excluirPopUp = document.querySelector('.excluirconta-popup')
const AddEnderecoPopUp = document.querySelector('.novoendereco-popup')

function abrirExcluir() {
    excluirPopUp.style.visibility = 'visible'
    excluirPopUp.style.opacity = '1'
}

function fecharExcluir() {
    excluirPopUp.style.visibility = 'hidden'
    excluirPopUp.style.opacity = '0'
}

function abrirAddEndereco() {
    AddEnderecoPopUp.style.visibility = 'visible'
    AddEnderecoPopUp.style.opacity = '1'
}

function fecharAddEndereco() {
    AddEnderecoPopUp.style.visibility = 'hidden'
    AddEnderecoPopUp.style.opacity = '0'
}