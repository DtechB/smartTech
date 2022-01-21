from django import forms
from django.contrib.auth.forms import UserCreationForm
from mainPage.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone',
                  'about', 'city', 'address']


class AvatarForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['img_avatar_upload']
        widgets = {
            'img_avatar_upload': forms.FileInput(),
        }


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')
