from django.urls import path
from . import views

urlpatterns = [
    path('movies_list/', views.MoviesListView.as_view(), name='movies_list'),
    path('movies_list/<int:id>/', views.MoviesDetailView.as_view(), name='movies_detail'),
    path('movies_list/<int:id>/delete/', views.DeleteMovieView.as_view(), name='delete_film'),
    path('movies_list/<int:id>/update/', views.EditFilmView.as_view(), name='edit_film'),
    path('create_film/', views.CreateMoviesView.as_view(), name='create_film'),
    path('create_review/', views.CreateMovieReviewView.as_view(), name='add_review'),
    path('search/', views.SearchView.as_view(), name='search'),
]
