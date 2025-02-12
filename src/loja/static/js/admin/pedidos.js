const successMessage = document.querySelector('.success')
const errorMessage = document.querySelector('.error')
const pageMessage = document.querySelector('.page-pedidos')
const editPedidoMessage = document.querySelector('.editar-pedido')
const editPedidoPopUp = document.querySelector('.editpedido-popup')

function abrirDetalhesPedido(id) {
    document.getElementById(`detalhespedido-popup-${id}`).style.visibility = 'visible';
    document.getElementById(`detalhespedido-popup-${id}`).style.opacity = '1';
}

function fecharDetalhesPedido(id) {
    document.getElementById(`detalhespedido-popup-${id}`).style.visibility = 'hidden';
    document.getElementById(`detalhespedido-popup-${id}`).style.opacity = '0';
}

function abrirEditPedido(id) {
    document.getElementById(`editpedido-popup-${id}`).style.visibility = 'visible';
    document.getElementById(`editpedido-popup-${id}`).style.opacity = '1';
}

function fecharEditPedido(id) {
    document.getElementById(`editpedido-popup-${id}`).style.visibility = 'hidden';
    document.getElementById(`editpedido-popup-${id}`).style.opacity = '0';
}

function abrirExcluirPedido(id) {
    document.getElementById(`excluirpedido-popup-${id}`).style.visibility = 'visible';
    document.getElementById(`excluirpedido-popup-${id}`).style.opacity = '1';
}

function fecharExcluirPedido(id) {
    document.getElementById(`excluirpedido-popup-${id}`).style.visibility = 'hidden';
    document.getElementById(`excluirpedido-popup-${id}`).style.opacity = '0';
}

if (pageMessage) {
    setTimeout(function() {
        window.location.href = pedidosUrl
    }, 1000)
}

if (editPedidoMessage) {
    editPedidoPopUp.style.visibility = 'visible'
    editPedidoPopUp.style.opacity = '1'
    if (successMessage) {
        setTimeout(function() {
            window.location.href = pedidosUrl
        }, 1000)
    } else if (errorMessage) {
        setTimeout(function() {
            window.location.href = pedidosUrl
        }, 2000)
    }
}