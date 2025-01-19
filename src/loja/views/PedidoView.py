from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def finalizar_pedido_view(request):
    return render(request, template_name='user/finalizar_pedido.html', status=200) 