from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.urls import reverse

def perfil_view(request):
    if request.user.is_authenticated:
        return render(request, template_name='perfil.html', status=200)
    else:
        return redirect('login')
    
def logout_view(request):
    logout(request)
    return redirect(reverse('home'))