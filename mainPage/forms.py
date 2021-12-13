from django import forms
from .models import User


class LoginForms(forms.Form):
    email = forms.EmailField()
    password = forms.PasswordInput()


class RegisterForms(forms.ModelForm):
    class Meta:
        user = User
        fields = ['first_name', 'last_name', 'email', 'password']


class ForgotForms(forms.ModelForm):
    class Meta:
        user = User
        fields = ['email']
