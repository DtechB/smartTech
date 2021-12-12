from django.shortcuts import render
from .models import SmartPhone, Post


def index(request):
    smartphones = SmartPhone.objects.select_related('SmartPhoneImgUrl').all()
    return render(request, 'mainPage/index.html')


def login(request):
    return render(request, 'mainPage/login.html')


def register(request):
    return render(request, 'mainPage/register.html')


def forgot(request):
    return render(request, 'mainPage/forgot-password.html')
