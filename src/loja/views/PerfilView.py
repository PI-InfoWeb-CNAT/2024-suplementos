from django.shortcuts import render, redirect

def perfil_view(request):
    if request.user.is_authenticated:
        return render(request, template_name='perfil.html', status=200)
    else:
        return redirect('login')

