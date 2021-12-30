from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from mainPage.models import SmartPhone


def index(request):
    phones = SmartPhone.objects.all()
    count_phone = request.user.smartphone_set.count()
    return render(request, 'phone/phone-content.html', context={
        'phones': phones,
        'count': count_phone
    })


def single_phone(request, phone, pk):
    phone = get_object_or_404(SmartPhone, slug=phone, pk=pk)
    return render(request, 'phone/phone-single.html', {'phones': phone})


def link(request, pk):
    user = request.user
    linke = get_object_or_404(SmartPhone, pk=pk)
    return JsonResponse({
        'phones': user.smartphone_set.count(),
        'user': user.is_authenticated
    })


def add_comparison_phone(request, pk):
    user = request.user
    linke = get_object_or_404(SmartPhone, pk=pk)
    if user.smartphone_set.count() <= 2:
        linke.user.add(user)
    return redirect('phone:phones')
