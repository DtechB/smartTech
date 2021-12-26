from django import forms
from mainPage.models import SmartPhone


class AddComparisonForm(forms.ModelForm):
    class Meta:
        model = SmartPhone
        fields = ['user']
