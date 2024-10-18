from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.urls import reverse
from loja.models import Cliente

def perfil_view(request):
    user = request.user
    clientes = Cliente.objects.all()

    if user.is_authenticated:
        nome = user.username
        email = user.email
        tel_celular = ''
        tel_fixo = ''
        cpf = ''

        for cliente in clientes:
            if cliente.id == user.id:
                cpf = cliente.CPF
                tel_celular = cliente.Telefone_celular
                tel_fixo = cliente.Telefone_fixo

        context = {
            'nome': nome,
            'email': email,
            'tel_celular': tel_celular,
            'tel_fixo': tel_fixo,
            'cpf': cpf
        }
        return render(request, template_name='perfil.html', context=context, status=200)
    else:
        return redirect('login')
    
def logout_view(request):
    logout(request)
    return redirect(reverse('home'))

def excluir_conta_view(request):
    if request.method == 'POST':
        user = request.user

        user.delete()
        logout(request)
        messages.success(request, 'Conta excluída com sucesso!')
        return redirect(reverse('home'))
    
    