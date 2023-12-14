from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Animal, Shelter
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group, User


#  форма для регистрации пользователя-приюта
class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='shelter_group')
        basic_group.user_set.add(user)
        return user


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


# форма создания приюта
class ShelterCreateForm(forms.ModelForm):

    class Meta:
        model = Shelter
        fields = [
            'name',
            'city',
            'year_of_foundation',
            'phone',
            'address',
            'link',
        ]


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


