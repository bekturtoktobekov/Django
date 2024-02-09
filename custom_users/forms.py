from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True, initial='+996',
                                   widget=forms.TextInput(attrs={'placeholder': 'Введите номер телефона'}))
    date_of_birth = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=models.GENDER_CHOICES)
    country = forms.ChoiceField(choices=models.COUNTRY)
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'phone_number',
            'date_of_birth',
            'gender',
            'country',
            'profile_picture'
        )

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.country = self.cleaned_data['country']
        user.profile_picture = self.cleaned_data['profile_picture']
        user.date_of_birth = self.cleaned_data['date_of_birth']
        if commit:
            user.save()
            return user