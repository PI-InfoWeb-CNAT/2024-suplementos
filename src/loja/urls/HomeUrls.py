from django.urls import path

from loja.views.HomeView import home_view
from loja.views.PromocoesView import promocoes_view
from loja.views.CadastroView import cadastro_view
from loja.views.LoginView import login_view
from loja.views.NotificacoesView import list_notificacoes_view, excluir_notificacoes_view

urlpatterns = [
    path("", home_view, name='home'),
    path("promocoes/", promocoes_view, name='promocoes'),
    path("cadastro/", cadastro_view, name='cadastro'),
    path("login/", login_view, name='login'),
    path("notificacoes/", list_notificacoes_view, name='notificacoes'),
    path("notificacoes/excluir", excluir_notificacoes_view, name='excluir-notificacoes'),
] 