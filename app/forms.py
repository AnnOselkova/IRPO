from django import forms
from .models import Animal, Shelter


class AnimalCreateForm(forms.ModelForm):

    class Meta:
        model = Animal
        fields = [
            'name',
            'date',
            'breed',
            'photo',
            'info',
            'sex',
            'category'
        ]


class ShelterLoginForm(forms.ModelForm):
    # model = Shelter
    # username = forms.CharField()
    # password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Shelter
        fields = [
            'email',
            'password'
        ]
