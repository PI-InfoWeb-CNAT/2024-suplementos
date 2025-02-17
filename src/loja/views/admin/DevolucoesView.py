from django.shortcuts import render

from loja.models import DevolucaoProduto

def list_devolucoes_view(request):
    devolucoes = DevolucaoProduto.objects.all()

    context = {
        'devolucoes': devolucoes
    }

    return render(request, 'admin/devolucoes.html', context=context, status=200)