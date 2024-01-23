from django.urls import path
from . import views

urlpatterns =[
    path('', views.persons_list, name='person_list'),
    path('persons_list/<int:id>/', views.persons_detail, name='person_detail'),
    path('persons_list/<int:id>/delete/', views.delete_person_view, name='person_delete'),
    path('persons_list/<int:id>/update/', views.edit_person_view, name='edit_person'),
    path('create_person/', views.create_person_view, name='create_person')
]