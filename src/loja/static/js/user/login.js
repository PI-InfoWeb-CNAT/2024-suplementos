const successMessage = document.querySelector('.success');
const errorMessage = document.querySelector('.error');
const RedefinirSenha = document.querySelector('.redefinir-senha-popup');
const btnEnviar = document.querySelector('.solicitacao-senha-popup');
const emailInput = document.getElementById('email-redefinir'); 

function abrir_redefinirsenha() {
    RedefinirSenha.style.visibility = 'visible';
    RedefinirSenha.style.opacity = '1';
}

function fechar_redefinirsenha() {
    RedefinirSenha.style.visibility = 'hidden';
    RedefinirSenha.style.opacity = '0';
}

function solicitacao_confirmada() {
    if (!emailInput.checkValidity()) {
        emailInput.reportValidity();
        return; 
    }
    RedefinirSenha.style.visibility = 'hidden';
    RedefinirSenha.style.opacity = '0';
    btnEnviar.style.visibility= 'visible';
    btnEnviar.style.opacity=1;
}

function fechar_solicitacao(){
    btnEnviar.style.visibility = 'hidden';
    btnEnviar.style.opacity = '0';
}

if (successMessage) {
    setTimeout(function() {
        window.location.href = homeUrl
    }, 2000);
} else if (errorMessage) {
    setTimeout(function() {
        window.location.href = loginUrl
    }, 1000);
}