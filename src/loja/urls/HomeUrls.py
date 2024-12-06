from django.urls import path

from loja.views.HomeView import home_view
from loja.views.PromocoesView import promocoes_view
from loja.views.CadastroView import cadastro_view
from loja.views.LoginView import login_view
from loja.views.NotificacoesView import list_notificacoes_view, excluir_notificacoes_view
from loja.views.FavoritoView import favorito_view
from loja.views.MeusFavoritosView import meusfavoritos_view
from loja.views.ProdutoView import produto_view
from loja.views.CarrinhoView import list_carrinho_view, create_carrinhoitem_view,  remover_item_view

urlpatterns = [
    path("", home_view, name='home'),
    path("promocoes/", promocoes_view, name='promocoes'),
    path("cadastro/", cadastro_view, name='cadastro'),
    path("login/", login_view, name='login'),
    path("produto/<int:id>", produto_view, name='produto'),
    path("favorito/", favorito_view, name='favorito'),
    path("meus-favoritos/", meusfavoritos_view, name='meus-favoritos'),
    path("notificacoes/", list_notificacoes_view, name='notificacoes'),
    path("notificacoes/excluir", excluir_notificacoes_view, name='excluir-notificacoes'),
    path("carrinho", list_carrinho_view, name='list_carrinho'),
    path('carrinho/remover/<int:item_id>/', remover_item_view, name='remover_carrinhoitem'),
    path("carrinho/<int:produto_id>", create_carrinhoitem_view, name='create_carrinhoitem'),
] 

