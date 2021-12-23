from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from mainPage.models import User, SmartPhone
from .forms import ProfileForm


@login_required
def home(request):
    queryset = SmartPhone.objects.filter(user=request.user)
    return render(request, 'account/panel.html', context={'phone': queryset})


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
