const cepInput = document.getElementById('cep-novoendereco')
const successMessage = document.querySelector('.success')
const errorMessage = document.querySelector('.error')
const dadosMessage = document.querySelector('.message-dados')
const redefinirSenhaMessage = document.querySelector('.message-redefinirsenha')
const novoEnderecoMessage = document.querySelector('.message-novoendereco')
const editEnderecoMessage = document.querySelector('.message-editendereco')
const redefinirSenhaPopUp = document.querySelector('.redefinirsenha-popup')
const editEnderecoPopUp = document.querySelector('.editendereco-popup')
const AddEnderecoPopUp = document.querySelector('.novoendereco-popup')
const excluirPopUp = document.querySelector('.excluirconta-popup')

function preencher() {
    cep = cepInput.value
    cep = cep.split('').filter(char => !isNaN(char) && char !== ' ').join('')
    
    
    let url = 'https://viacep.com.br/ws/' + cep + '/json/';

    fetch(url)
    .then(response => response.json())
    .then(data => {
        if (!data.erro) {
            document.getElementById('rua-novoendereco').value = data.logradouro;
            document.getElementById('cidade-novoendereco').value = data.localidade;
            document.getElementById('estado-novoendereco').value = data.uf;
        } else {
            alert('CEP não encontrado!');
        }
    })
    .catch(error => {
        alert('Erro ao buscar o CEP. Verifique o CEP digitado ou tente novamente.');
        console.error(error);
    });
}

function abrirRedefinirSenha() {
    redefinirSenhaPopUp.style.visibility = 'visible'
    redefinirSenhaPopUp.style.opacity = '1'
}

function fecharRedefinirSenha() {
    redefinirSenhaPopUp.style.visibility = 'hidden'
    redefinirSenhaPopUp.style.opacity = '0'
}

function abrirEditEndereco(id) {
    document.getElementById(`editendereco-popup-${id}`).style.visibility = 'visible';
    document.getElementById(`editendereco-popup-${id}`).style.opacity = '1';
}

function fecharEditEndereco(id) {
    document.getElementById(`editendereco-popup-${id}`).style.visibility = 'hidden';
    document.getElementById(`editendereco-popup-${id}`).style.opacity = '0';
}

function abrirAddEndereco() {
    AddEnderecoPopUp.style.visibility = 'visible'
    AddEnderecoPopUp.style.opacity = '1'
}

function fecharAddEndereco() {
    AddEnderecoPopUp.style.visibility = 'hidden'
    AddEnderecoPopUp.style.opacity = '0'
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
} else if (novoEnderecoMessage) {
    AddEnderecoPopUp.style.visibility = 'visible'
    AddEnderecoPopUp.style.opacity = '1'
    setTimeout(function() {
        window.location.href = perfilUrl
    }, 1000)
} else if (editEnderecoMessage) {
    editEnderecoPopUp.style.visibility = 'visible'
    editEnderecoPopUp.style.opacity = '1'
    setTimeout(function() {
        window.location.href = perfilUrl
    }, 1000)
}