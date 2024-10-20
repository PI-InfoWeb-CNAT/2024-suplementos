const excluirPopUp = document.querySelector('.excluirconta-popup')
const AddEnderecoPopUp = document.querySelector('.novoendereco-popup')
const successMessage = document.querySelector('.success')
const errorMessage = document.querySelector('.error')
const dadosMessage = document.getElementById('messages-dados')

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

// if (successMessage && dadosMessage) {
//     setTimeout(function() {
//         window.location.href = "{% url 'perfil' %}"
//     }, 2000)
// } else if (errorMessage && dadosMessage) {
//     setTimeout(function() {
//         window.location.href = "{% url 'perfil' %}"
//     }, 2000)
// } 