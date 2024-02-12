from django.db import models

class HashTag(models.Model):
    name = models.CharField(max_length=100, verbose_name='Напишите хегтег', default='#')

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название продукта')
    description = models.TextField(blank=True, verbose_name='Описание продукта')
    price = models.PositiveIntegerField(verbose_name='Укажите цену продукта')
    tags = models.ManyToManyField(HashTag)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='Напишите тег', default='#')

    def __str__(self):
        return self.name

class ProductClothes(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название одежды')
    description = models.TextField(blank=True, verbose_name='Описание продукта')
    price = models.PositiveIntegerField(verbose_name='Укажите цену одежды')
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

