from django.http import HttpResponse

from loja.models import Produto

def list_produto_view(request, id=None):
    produto = request.GET.get("produto")
    destaque = request.GET.get("destaque")
    promocao = request.GET.get("promocao")
    categoria = request.GET.get("categoria")
    fabricante = request.GET.get("fabricante")

    produtos = Produto.objects.all()
    print(produtos)
    if id is None:
        id = 0
    return HttpResponse('<h1>Produto de id %s!</h1>' % id)