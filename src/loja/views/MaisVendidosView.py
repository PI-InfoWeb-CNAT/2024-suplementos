from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse

def maisvendidos_view(request):
    return render(request, template_name='user/maisvendidos.html', status=200)