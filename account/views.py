from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, CreateView
from mainPage.models import User, SmartPhone
from .forms import ProfileForm


@login_required
def home(request):
    queryset = SmartPhone.objects.filter(user=request.user)
    return render(request, 'account/panel.html', context={'phone': queryset})


class Profile(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'account/profile.html'
    form_class = ProfileForm

    def get_object(self, queryset=None):
        return User.objects.get(pk=self.request.user.pk)
