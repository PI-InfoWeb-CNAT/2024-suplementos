from django.urls import path

from loja.views.HomeView import home_view
from loja.views.PromocoesView import promocoes_view
from loja.views.CadastroView import cadastro_view
from loja.views.LoginView import login_view, logout_view

urlpatterns = [
    path("", home_view, name='home'),
    path("promocoes/", promocoes_view, name='promocoes'),
    path("cadastro/", cadastro_view, name='cadastro'),
    path("login/", login_view, name='login'),
    path("logout/", logout_view, name='logout'),
] 