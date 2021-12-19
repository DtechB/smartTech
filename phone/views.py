from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from mainPage.models import SmartPhone, SmartPhoneImgUrl


def index(request):

    phones = SmartPhone.objects.all()
    return render(request, 'phone/phone-content.html', context={
        'phones': phones
    })


def single_phone(request, phone, pk):
    phone = get_object_or_404(SmartPhone, slug=phone, pk=pk)
    return render(request, 'phone/phone-single.html', {'phones': phone})
