from django import forms
from mainPage.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone',
                  'about', 'city', 'address', 'img_avatar_upload']
        widgets = {
            'img_avatar_upload': forms.FileInput(),
        }
