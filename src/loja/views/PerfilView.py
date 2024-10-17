from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.urls import reverse
from loja.models import Cliente

def perfil_view(request):
    user = request.user
    clientes = Cliente.objects.all()

    if user.is_authenticated:
        email = user.email
        tel_celular = ''
        tel_fixo = ''

        for cliente in clientes:
            if cliente.id == user.id:
                tel_celular = cliente.Telefone_celular
                tel_fixo = cliente.Telefone_fixo

        context = {
            'email': email,
            'tel_celular': tel_celular,
            'tel_fixo': tel_fixo
        }
        return render(request, template_name='perfil.html', context=context, status=200)
    else:
        return redirect('login')
    
def logout_view(request):
    logout(request)
    return redirect(reverse('home'))