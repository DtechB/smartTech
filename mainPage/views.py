from django.shortcuts import render
from .models import SmartPhone, Post
from .forms import LoginForms, RegisterForms, ForgotForms


def index(request):
    phones = SmartPhone.objects.all()[:3]
    return render(request, 'mainPage/index.html', context={'phones': phones})
