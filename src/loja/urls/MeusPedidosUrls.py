from django.urls import path

from loja.views.MeusPedidosView import meuspedidos_view, cancelar_pedido_view, confirmar_recebimento_view
from loja.views.AvaliarProdutoView import avaliar_produto_view
from loja.views.DevolverProdutoView import devolver_produto_view

urlpatterns = [
    path('', meuspedidos_view, name='meus-pedidos'),
    path('cancelar-pedido/', cancelar_pedido_view, name='cancelar-pedido'),
    path('avaliar-produto/', avaliar_produto_view, name='avaliar-produto'),
    path('devolver-produto/', devolver_produto_view, name='devolver-produto'),
    path('confirmar-recebimento/', confirmar_recebimento_view, name='confirmar-recebimento'),
] 