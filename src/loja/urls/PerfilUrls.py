from django.urls import path

from loja.views.PerfilView import perfil_view

urlpatterns = [
    path('', perfil_view, name='perfil'),
]