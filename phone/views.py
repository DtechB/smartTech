from django.shortcuts import render, get_object_or_404
from mainPage.models import SmartPhone
from .forms import AddComparisonForm


def index(request):
    phones = SmartPhone.objects.all()
    if request.method == 'POST':
        form = AddComparisonForm(request.POST)
        if form.is_valid():
            phone_id = request.POST.get('id')
            phone = SmartPhone.objects.get(smartphone_id=phone_id)
            user = request.user
            if user.smartphone_set.count() <= 2:
                phone.user.add(user)
    else:
        form = AddComparisonForm()

    return render(request, 'phone/phone-content.html', context={
        'phones': phones,
        'form': form
    })


def single_phone(request, phone, pk):
    phone = get_object_or_404(SmartPhone, slug=phone, pk=pk)
    return render(request, 'phone/phone-single.html', {'phones': phone})
