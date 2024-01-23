from django import forms
from . import models

class TekkenForm(forms.ModelForm):
    class Meta:
        model = models.PersonsGame
        fields = '__all__'