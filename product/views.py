from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404
from . import models

class ProductDrinksList(generic.ListView):
    template_name = 'products/products_drink_list.html'
    context_object_name = 'drinks_list'
    model = models.Product

    def get_queryset(self):
        return self.model.objects.filter(tags__name='#напитки').order_by("-id")

class ProductDishesList(generic.ListView):
    template_name = 'products/products_dishes_list.html'
    context_object_name = 'dishes_list'
    model = models.Product

    def get_queryset(self):
        return self.model.objects.filter(tags__name='#еда').order_by("-id")

class ClothesList(generic.ListView):
    template_name = 'products/clothes_list.html'
    context_object_name = 'clothes_list'
    model = models.ProductClothes

    def get_queryset(self):
        return self.model.objects.filter(tags__name='#для детей').order_by("-id")