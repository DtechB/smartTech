from django.shortcuts import render
from .models import SmartPhone, Post
from .forms import LoginForms, RegisterForms, ForgotForms


def index(request):
    phones = SmartPhone.objects.all()[:3]
    return render(request, 'mainPage/index.html', context={'phones': phones})


def register(request):
    return render(request, 'mainPage/register.html')


def forgot(request):
    return render(request, 'mainPage/forgot-password.html')
