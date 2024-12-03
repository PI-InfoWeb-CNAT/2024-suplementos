from django.urls import path

from loja.views.HomeView import home_view
from loja.views.PromocoesView import promocoes_view
from loja.views.CadastroView import cadastro_view
from loja.views.LoginView import login_view
from loja.views.CarrinhoView2 import carrinho_view, adicionarcarrinho_view
from loja.views.NotificacoesView import list_notificacoes_view, excluir_notificacoes_view
from loja.views.FavoritoView import favorito_view
from loja.views.MeusFavoritosView import meusfavoritos_view

urlpatterns = [
    path("", home_view, name='home'),
    path("promocoes/", promocoes_view, name='promocoes'),
    path("cadastro/", cadastro_view, name='cadastro'),
    path("login/", login_view, name='login'),
    path("favorito/", favorito_view, name='favorito'),
    # path("carrinho/", carrinho_view, name='carrinho'),
    # path("adicionar-carrinho/", adicionarcarrinho_view, name='adicionarcarrinho'),
    path("meus-favoritos/", meusfavoritos_view, name='meus-favoritos'),
    path("notificacoes/", list_notificacoes_view, name='notificacoes'),
    path("notificacoes/excluir", excluir_notificacoes_view, name='excluir-notificacoes'),
] 