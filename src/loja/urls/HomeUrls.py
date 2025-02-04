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
from loja.views.user.PedidoView import finalizar_pedido_view
from loja.views.user.MaisVendidosView import maisvendidos_view
from loja.views.user.ComprarNovamenteView import comprar_novamente_view

from loja.views.admin.ProdutosView import produtosAdmin_view, excluir_produto_view

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
    path("produtos/", produtosAdmin_view, name='produtos'),
    path("produtos/excluir", excluir_produto_view, name='excluir-produto'),
] 