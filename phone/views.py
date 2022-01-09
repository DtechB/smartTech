from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from mainPage.models import SmartPhone, SmartPhoneImgUrl, SmartPhoneDescription, Offer


def index(request):
    phones = SmartPhone.objects.all()
    count_phone = None
    if request.user.is_authenticated:
        count_phone = request.user.smartphone_set.count()

    return render(request, 'phone/phone-content.html', context={
        'phones': phones,
        'count': count_phone
    })


def single_phone(request, phone, pk):
    phone = get_object_or_404(SmartPhone, slug=phone, pk=pk)
    img_phone = SmartPhoneImgUrl.objects.filter(smartphone=phone)
    description = SmartPhoneDescription.objects.filter(smartphone=phone)
    offers = Offer.objects.filter(smartphone=phone).first()
    return render(request, 'phone/phone-single.html', {
        'phones': phone,
        'imagephone': img_phone,
        'desc': description,
        'offers': offers
    })


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
