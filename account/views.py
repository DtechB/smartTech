from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from mainPage.models import User, SmartPhone, Post
from .forms import ProfileForm
from django.http import HttpResponse, JsonResponse
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage


@login_required
def home(request):
    queryset1 = SmartPhone.objects.filter(user=request.user)
    queryset2 = Post.objects.filter(userpost=request.user)
    queryset3 = Post.objects.order_by('-updated').all()[:6]
    return render(request, 'account/panel.html', context={
        'phone': queryset1,
        'posts': queryset2,
        'all_posts': queryset3
    })


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('account:panel')
    else:
        form = ProfileForm(instance=request.user)

    return render(request, 'account/profile.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('registration/activate_acc.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return render(request, 'registration/base_inform.html', context={
                'title': 'Confirm Email',
                'des': 'Please confirm your email address to complete the registration '
            })
    else:
        form = SignupForm()
    return render(request, 'registration/register.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'registration/base_inform.html', context={
            'title': 'Successfully Confirm',
            'des': 'Thank you for your email confirmation. Now you can login your account '
        })
    else:
        return HttpResponse('Activation link is invalid!')


@login_required
def comparison(request):
    queryset = SmartPhone.objects.filter(user=request.user).all()
    return render(request, 'account/comparison.html', context={
        'phones': queryset
    })


def remove_comparison_phone(request, pk):
    user = request.user
    linke = get_object_or_404(SmartPhone, pk=pk)
    if user.smartphone_set.count() != 0:
        linke.user.remove(user)
    return redirect('account:comparison')
