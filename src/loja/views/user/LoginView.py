from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login

from .CarrinhoView import migrar_carrinho_para_usuario

def login_view(request):
    session_key =  request.session.session_key
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        if email and senha:
            try:
                user = User.objects.get(email=email)
                
                if user.check_password(senha):
                    user = authenticate(request, username=user.username, password=senha)
                else:
                    user = None

            except User.DoesNotExist:
                user = None

            if user is not None:
                auth_login(request, user)
                migrar_carrinho_para_usuario(user, session_key)

                _next = request.GET.get('next')
                if _next is not None:
                    messages.success(request, 'Login realizado com sucesso!', extra_tags='page-login')
                    return redirect(_next)
                else:
                    messages.success(request, 'Login realizado com sucesso!', extra_tags='page-login')
            else:
                messages.error(request, 'Email ou senha inválidos!', extra_tags='page-login')
        else:
            messages.error(request, 'Preencha todos os campos!', extra_tags='page-login')

    return render(request, template_name='user/login.html', status=200) 