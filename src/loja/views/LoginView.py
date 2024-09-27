from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.urls import reverse

def login_view(request):
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
                messages.success(request, 'Login realizado com sucesso!')
            else:
                messages.error(request, 'Email ou senha inválidos!')
        else:
            messages.error(request, 'Preencha todos os campos!')

    return render(request, template_name='login.html', status=200) 

def logout_view(request):
    logout(request)
    return redirect(reverse('home'))