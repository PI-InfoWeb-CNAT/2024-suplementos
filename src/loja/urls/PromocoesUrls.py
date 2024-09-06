from django.urls import path

from loja.views.PromocoesView import promocoes_view

urlpatterns = [
    path("", promocoes_view, name='promocoes'),
] 