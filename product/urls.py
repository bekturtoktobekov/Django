from django.urls import path
from . import views

urlpatterns = [
    path('product_drinks/', views.ProductDrinksList.as_view(), name='drinks_list'),
    path('product_dishes/', views.ProductDishesList.as_view(), name='dishes_list'),
    path('clothes_product/', views.ClothesList.as_view(), name='clothes_list')
]