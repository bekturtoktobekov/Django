from django.contrib import admin
from . import models

admin.site.register(models.Product)
admin.site.register(models.HashTag)
admin.site.register(models.ProductClothes)
admin.site.register(models.Tag)
