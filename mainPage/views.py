from django.shortcuts import render, redirect
from .models import SmartPhone, Post, User
from django.core.mail import EmailMessage


def index(request):
    phones = SmartPhone.objects.all()[:3]
    posts = Post.objects.all()[:3]
    phones_number = SmartPhone.objects.all().count()
    posts_number = Post.objects.all().count()
    users_number = User.objects.all().count()

    if request.method == 'POST':
        name = request.POST.get('name')
        mail_subject = request.POST.get('subject')
        message = f'Hi {name} dear,\n\n' \
                  + request.POST.get('message') \
                  + '\n\n we check your question and You will be answered as soon as ' \
                    'possible after the review.\nThanks, SmartTech.'
        to_email = request.POST.get('email')
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()
        return redirect('account:contact_sent')

    return render(request, 'mainPage/index.html', context={
        'phones': phones,
        'posts': posts,
        'user_count': users_number,
        'post_count': posts_number,
        'phone_count': phones_number,
    })


def not_found_404(request, exception):
    return render(request, 'not_found_404.html')
