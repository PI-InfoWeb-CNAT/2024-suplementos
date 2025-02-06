const cancelarPedidoPopUp = document.querySelector('.cancelarpedido-popup')
const detalhesPedidoPopUp = document.querySelector('.detalhespedido-popup')
const confirmarRecebimentoPopUp = document.querySelector('.confirmarrecebimento-popup')
const avaliarProdutoPopUp = document.querySelector('.avaliarproduto-popup')
const devolverProdutoPopUp = document.querySelector('.devolverproduto-popup')
const pageMessage = document.querySelector('.page-meuspedidos')

function abrirCancelarPedido(id) {
    document.getElementById(`cancelarpedido-popup-${id}`).style.visibility = 'visible';
    document.getElementById(`cancelarpedido-popup-${id}`).style.opacity = '1';
}
function fecharCancelarPedido(id) {
    document.getElementById(`cancelarpedido-popup-${id}`).style.visibility = 'hidden';
    document.getElementById(`cancelarpedido-popup-${id}`).style.opacity = '0';
}

function abrirDetalhesPedido(id) {
    document.getElementById(`detalhespedido-popup-${id}`).style.visibility = 'visible';
    document.getElementById(`detalhespedido-popup-${id}`).style.opacity = '1';
}
function fecharDetalhesPedido(id) {
    document.getElementById(`detalhespedido-popup-${id}`).style.visibility = 'hidden';
    document.getElementById(`detalhespedido-popup-${id}`).style.opacity = '0';
}

function abrirConfirmarRecebimento(id) {
    document.getElementById(`confirmarrecebimento-popup-${id}`).style.visibility = 'visible';
    document.getElementById(`confirmarrecebimento-popup-${id}`).style.opacity = '1';
}
function fecharConfirmarRecebimento(id) {
    document.getElementById(`confirmarrecebimento-popup-${id}`).style.visibility = 'hidden';
    document.getElementById(`confirmarrecebimento-popup-${id}`).style.opacity = '0';
}

function abrirAvaliarProduto(id) {
    document.getElementById(`avaliarproduto-popup-${id}`).style.visibility = 'visible';
    document.getElementById(`avaliarproduto-popup-${id}`).style.opacity = '1';
}
function fecharAvaliarProduto(id) {
    document.getElementById(`avaliarproduto-popup-${id}`).style.visibility = 'hidden';
    document.getElementById(`avaliarproduto-popup-${id}`).style.opacity = '0';
}

function abrirDevolverProduto(id) {
    document.getElementById(`devolverproduto-popup-${id}`).style.visibility = 'visible';
    document.getElementById(`devolverproduto-popup-${id}`).style.opacity = '1';
}
function fecharDevolverProduto(id) {
    document.getElementById(`devolverproduto-popup-${id}`).style.visibility = 'hidden';
    document.getElementById(`devolverproduto-popup-${id}`).style.opacity = '0';
}

if (pageMessage) {
    setTimeout(function() {
        window.location.href = meusPedidosUrl
    }, 1000)
}