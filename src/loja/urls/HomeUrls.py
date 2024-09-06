from django.urls import path

from loja.views.HomeView import home_view

urlpatterns = [
    path("", home_view, name='home'),
] 