from django.shortcuts import render, redirect
from django.contrib import messages
from loja.models import Cliente
from django.contrib.auth.models import User
from django.urls import reverse

def cadastro_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome_usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        cpf = request.POST.get('cpf')
        tel_celular = request.POST.get('tel_celular')
        tel_fixo = request.POST.get('tel_fixo')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'E-mail já cadastrado')
        elif Cliente.objects.filter(CPF=cpf).exists():
            messages.error(request, 'CPF já cadastrado')
        elif Cliente.objects.filter(Telefone_celular=tel_celular).exists():
            messages.error(request, 'Telefone celular já cadastrado')
        else:
            user = User.objects.create_user(username=nome, email=email, password=senha)
            user.save()
            Cliente.objects.create(
                user=user,
                Nome=nome,
                CPF=cpf,
                Telefone_celular=tel_celular,
                Telefone_fixo=tel_fixo
            )
            messages.success(request, 'Cadastro realizado com sucesso')

    return render(request, template_name='cadastro.html', status=200)