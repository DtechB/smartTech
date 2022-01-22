from django.shortcuts import render
from .models import SmartPhone, Post, User
from .forms import LoginForms, RegisterForms, ForgotForms


def index(request):
    phones = SmartPhone.objects.all()[:3]
    posts = Post.objects.all()[:3]
    phones_number = SmartPhone.objects.all().count()
    posts_number = Post.objects.all().count()
    users_number = User.objects.all().count()
    return render(request, 'mainPage/index.html', context={
        'phones': phones,
        'posts': posts,
        'user_count': users_number,
        'post_count': posts_number,
        'phone_count': phones_number,
    })


def not_found_404(request, exception):
    return render(request, 'not_found_404.html')
