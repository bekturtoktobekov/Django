from django import forms
from . import models

class MoviesForm(forms.ModelForm):
    class Meta:
        model = models.Movies
        fields = '__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = '__all__'