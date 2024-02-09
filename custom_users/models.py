from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICES = (
    ('MALE', "MALE"),
    ('FEMALE', "FEMALE"),
    ('OTHER', "OTHER")
)

COUNTRY = (
    ('KGZ', 'Kyrgyzstan'),
    ('USA', 'United States'),
    ('CAN', 'Canada'),
    ('GBR', 'United Kingdom'),
    ('KZ', 'Kazakhstan'),
    ('UZB', 'Uzbekistan'),
    ('KR', 'South Korea'),
    ('RUS', 'Russia'),
    ('JP', 'Japam')
)

class CustomUser(User):
    phone_number = models.CharField(max_length=30, default='+996')
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    country = models.CharField(max_length=50, choices=COUNTRY)


