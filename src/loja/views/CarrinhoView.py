from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def carrinho_view(request):
    
    return render(request, template_name='home.html', status=200)