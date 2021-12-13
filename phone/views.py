from django.db.models import Count
from django.shortcuts import render
from mainPage.models import SmartPhone, SmartPhoneImgUrl


def index(request):
    nums = [i for i in range(3, 61, 3)]
    phones = SmartPhone.objects.filter(smartphoneimgurl__id__in=nums).values('name', 'brand',
                                                                             'smartphoneimgurl__img_url',
                                                                             'smartphoneimgurl__id')
    return render(request, 'phone/phone-content.html', context={
        'phones': phones
    })


def single_phone(request):
    return render(request, 'phone/phone-single.html')
