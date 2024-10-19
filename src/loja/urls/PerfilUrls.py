from django.urls import path

from loja.views.PerfilView import perfil_view, edit_dados_view, logout_view, excluir_conta_view

urlpatterns = [
    path('', perfil_view, name='perfil'),
    path('edit/', edit_dados_view, name='edit'),
    path('logout/', logout_view, name='logout'),
    path('excluir/', excluir_conta_view, name='excluir'),
]