from django.shortcuts import render

def login_view(request):
    return render(request, template_name='login.html', status=200) 