from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from loja.models import Cliente

@login_required
def perfil_view(request):
    user = request.user
    clientes = Cliente.objects.all()

    nome = user.username
    email = user.email
    tel_celular = ''
    cpf = ''

    for cliente in clientes:
        if cliente.id == user.id:
            cpf = cliente.CPF
            tel_celular = cliente.Telefone_celular

    context = {
        'nome': nome,
        'email': email,
        'tel_celular': tel_celular,
        'cpf': cpf
    }
    return render(request, template_name='perfil.html', context=context, status=200)

@login_required 
def edit_dados_view(request):
    user = request.user

    cliente = Cliente.objects.get(user=user)

    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        tel_celular = request.POST.get('tel_celular')

        user.username = nome
        user.email = email
        user.save()

        cliente.Telefone_celular = tel_celular
        cliente.save()

        messages.success(request, 'Dados atualizados com sucesso!')
        return render(request, template_name='perfil.html', status=200)
    
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
    
    