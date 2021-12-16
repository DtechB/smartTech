from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from mainPage.models import User, SmartPhone


@login_required
def home(request):
    queryset = SmartPhone.objects.filter(user_id=1)
    return render(request, 'account/panel.html', context={'phone': queryset})
