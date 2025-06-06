from django.urls import path

from loja.views.user.PerfilView import perfil_view, edit_dados_view, redefinir_senha_view, logout_view, excluir_conta_view
from loja.views.user.EnderecoView import adicionar_endereco_view, edit_endereco_view, excluir_endereco_view
from loja.views.user.CarteiraView import list_carteira_view, adicionar_cartao_view, edit_cartao_view, excluir_cartao_view

urlpatterns = [
    path('', perfil_view, name='perfil'),
    path('edit/', edit_dados_view, name='edit-dados'),
    path('adicionar-endereco/', adicionar_endereco_view, name='adicionar-endereco'),
    path('edit-endereco/', edit_endereco_view, name='edit-endereco'),
    path('redefinir-senha/', redefinir_senha_view, name='redefinir-senha'),
    path('excluir-endereco/', excluir_endereco_view, name='excluir-endereco'),
    path('logout/', logout_view, name='logout'),
    path('excluir-conta/', excluir_conta_view, name='excluir-conta'),
    path('minha-carteira/', list_carteira_view, name='minha-carteira'),
    path('minha-carteira/adicionar-cartao', adicionar_cartao_view, name='adicionar-cartao'),
    path('minha-carteira/edit-cartao', edit_cartao_view, name='edit-cartao'),
    path('minha-carteira/excluir-cartao', excluir_cartao_view, name='excluir-cartao'),
]