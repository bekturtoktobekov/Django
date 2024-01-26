from django.urls import path
from . import views

urlpatterns = [
    path('movies_list/', views.movies_list, name='movies_list'),
    path('movies_list/<int:id>/', views.movies_detail, name='movies_detail'),
    path('movies_list/<int:id>/delete/', views.delete_film, name='delete_film'),
    path('movies_list/<int:id>/update/', views.edit_film, name='edit_film'),
    path('create_film/', views.create_new_film, name='create_film'),
    path('create_review/', views.add_review, name='create_review'),
    path('see_review/', views.list_review, name='see_review')
]
