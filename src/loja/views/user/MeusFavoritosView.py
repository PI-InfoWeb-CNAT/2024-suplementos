from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from loja.models import Produto

@login_required
def meusfavoritos_view(request):
    produtos = Produto.objects.all()

    context = {'produtos': produtos}

    return render(request, template_name='user/meusfavoritos.html', context=context, status=200)