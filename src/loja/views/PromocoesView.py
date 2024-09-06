from django.shortcuts import render
from loja.models import Produto

def promocoes_view(request):
    produtos = Produto.objects.all()
 
    context = {'produtos': produtos}
    return render(request, template_name='promocoes.html', context=context, status=200)