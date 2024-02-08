from django import forms
from . import models, parser

class ParserForm(forms.ModelForm):
    MEDIA_CHOICES = (
        ('mashinakg', 'mashinakg'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        model = models.MashinakgItems  # Specify the model class
        fields = ['media_type', ]

    def parser_data(self):
        if self.cleaned_data['media_type'] == 'mashinakg':  # Use cleaned_data to access form data
            mashinakg = parser.parser()
            for item in mashinakg:
                models.MashinakgItems.objects.create(**item)  # Use item instead of i
