from django.urls import path

from loja.views.HomeView import home_view
from loja.views.PromocoesView import promocoes_view
from loja.views.CadastroView import cadastro_view
from loja.views.LoginView import login_view
from loja.views.NotificacoesView import list_notificacoes_view, excluir_notificacoes_view
from loja.views.FavoritoView import favorito_view
from loja.views.MeusFavoritosView import meusfavoritos_view
from loja.views.ProdutoView import produto_view, produtosAdmin_view, excluir_produto_view
from loja.views.CategoriaView import categoria_view
from loja.views.CarrinhoView import adicionar_ao_carrinho, listar_carrinho_view, remover_item_view

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

    # ADMIN
    path("produtos/", produtosAdmin_view, name='produtos'),
    path("produtos/excluir", excluir_produto_view, name='excluir-produto'),
] 