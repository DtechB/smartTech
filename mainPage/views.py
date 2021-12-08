from django.shortcuts import render


def index(request):
    return render(request, 'mainPage/index.html')


def login(request):
    return render(request, 'mainPage/login.html')


def register(request):
    return render(request, 'mainPage/register.html')


def forgot(request):
    return render(request, 'mainPage/forgot-password.html')
