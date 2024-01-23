from django.urls import path
from . import views

urlpatterns = [
    path('movies_list/', views.movies_list, name='movies_list'),
    path('movies_list/<int:id>/', views.movies_detail, name='movies_detail'),
]
