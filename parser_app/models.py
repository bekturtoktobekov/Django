from django.db import models

class MashinakgItems(models.Model):
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=50)
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.title