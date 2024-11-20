from django.shortcuts import render

def list_carteira_view(request):
    return render(request, template_name='Perfil/carteira.html', status=200)