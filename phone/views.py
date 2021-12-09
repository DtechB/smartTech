from django.shortcuts import render


def index(request):
    return render(request, 'phone/phone-content.html')


def single_phone(request):
    return render(request, 'phone/phone-single.html')
