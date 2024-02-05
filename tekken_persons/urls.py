from django.urls import path
from . import views

urlpatterns =[
    path('', views.PersonsListView.as_view(), name='person_list'),
    path('persons_list/<int:id>/', views.PersonsDetailView.as_view(), name='person_detail'),
    path('persons_list/<int:id>/delete/', views.DeletePersonView.as_view(), name='person_delete'),
    path('persons_list/<int:id>/update/', views.EditPersonView.as_view(), name='edit_person'),
    path('create_person/', views.CreatePersonView.as_view(), name='create_person')
]