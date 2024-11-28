from django.shortcuts import render, redirect
from django.urls import reverse

from loja.models import Favorito


def favorito_view(request):
    favoritos = Favorito.objects.all()

    if request.method == 'POST':
        produto_id = request.POST.get('produto_id')
        
        
    return redirect(reverse('home'))