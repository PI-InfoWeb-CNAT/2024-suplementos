from django.urls import path

from loja.views.HomeView import home_view
from loja.views.user.PromocoesView import promocoes_view
from loja.views.user.CadastroView import cadastro_view
from loja.views.user.LoginView import login_view
from loja.views.user.NotificacoesView import list_notificacoes_view, excluir_notificacoes_view
from loja.views.user.FavoritoView import favorito_view
from loja.views.user.MeusFavoritosView import meusfavoritos_view
from loja.views.user.ProdutoView import produto_view
from loja.views.user.CategoriaView import categoria_view
from loja.views.user.CarrinhoView import adicionar_ao_carrinho, listar_carrinho_view, remover_item_view
from loja.views.user.FinalizarPedidoView import finalizar_pedido_view
from loja.views.user.MaisVendidosView import maisvendidos_view
from loja.views.user.ComprarNovamenteView import comprar_novamente_view

from loja.views.admin.ProdutosView import produtos_view, criar_produto_view, edit_produto_view, excluir_produto_view
from loja.views.admin.LotesView import list_lotes_view, criar_lote_view, edit_lote_view, excluir_lote_view
from loja.views.admin.PedidosView import list_pedidos_view, edit_pedido_view, excluir_pedido_view
from loja.views.admin.NotificacoesView import list_notificacoesAdmin_view, criar_notificacao_view, edit_notificacao_view, excluir_notificacao_view
from loja.views.admin.DevolucoesView import list_devolucoes_view

urlpatterns = [
    # USER
    path("", home_view, name='home'),
    path("promocoes/", promocoes_view, name='promocoes'),
    path("cadastro/", cadastro_view, name='cadastro'),
    path("login/", login_view, name='login'),
    path("produto/<int:id>/", produto_view, name='produto'),
    path("categoria/<str:categoria>/", categoria_view, name='categoria'),
    path("favorito/", favorito_view, name='favorito'),
    path("meus-favoritos/", meusfavoritos_view, name='meus-favoritos'),
    path("notificacoes/", list_notificacoes_view, name='notificacoes'),
    path("notificacoes/excluir", excluir_notificacoes_view, name='excluir-notificacoes'),
    path("carrinho/", listar_carrinho_view, name='carrinho'),
    path("carrinho/<int:idProduto>", adicionar_ao_carrinho, name='adicionar-ao-carrinho'),
    path("carrinho/remover-item/<int:idItem>", remover_item_view, name='remover-item'),
    path("finalizar-pedido/", finalizar_pedido_view, name='finalizar-pedido'),
    path("mais-vendidos", maisvendidos_view, name='mais-vendidos'),
    path("comprar-novamente", comprar_novamente_view, name='comprar-novamente'),

    # ADMIN
    path("produtos/", produtos_view, name='produtos'),
    path("produtos/criar", criar_produto_view, name='criar-produto'),
    path("produtos/editar", edit_produto_view, name='edit-produto'),
    path("produtos/excluir", excluir_produto_view, name='excluir-produto'),
    path("lotes", list_lotes_view, name='lotes'),
    path("lotes/criar", criar_lote_view, name='criar-lote'),
    path("lotes/editar", edit_lote_view, name='edit-lote'),
    path("lotes/excluir", excluir_lote_view, name='excluir-lote'),
    path("pedidos", list_pedidos_view, name='pedidos'),
    path("pedidos/editar", edit_pedido_view, name='edit-pedido'),
    path("pedidos/excluir", excluir_pedido_view, name='excluir-pedido'),
    path("pedidos/excluir", excluir_pedido_view, name='excluir-pedido'),
    path("notificacoes-admin", list_notificacoesAdmin_view, name='notificacoes-admin'),
    path("notificacoes-admin/criar", criar_notificacao_view, name='criar-notificacao'),
    path("notificacoes-admin/editar", edit_notificacao_view, name='edit-notificacao'),
    path("notificacoes-admin/excluir", excluir_notificacao_view, name='excluir-notificacao'),
    path("devolucoes", list_devolucoes_view, name='devolucoes'),
] 