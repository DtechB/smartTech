from django import forms
from mainPage.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'membership',
                  'birth_date', 'img_avatar_upload', 'about', 'city', 'address']
