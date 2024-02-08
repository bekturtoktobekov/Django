from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.http import HttpResponse
from django.views import generic

class MoviesListView(generic.ListView):
    model = models.Movies
    template_name = 'films/movies_list.html'
    context_object_name = 'movies'

    def get_queryset(self):
        return self.model.objects.all()


# def movies_list(request):
#     if request.method == 'GET':
#         movies = models.Movies.objects.all()
#         return render(request, template_name='films/movies_list.html',
#                       context={'movies' : movies})

class MoviesDetailView(generic.DetailView):
    template_name = 'films/movies_detail.html'
    context_object_name = 'details'

    def get_object(self, **kwargs):
        movies_id = self.kwargs.get('id')
        return get_object_or_404(models.Movies, id=movies_id)

# def movies_detail(request, id):
#     if request.method == 'GET':
#         details = get_object_or_404(models.Movies, id=id)
#         return render(request, template_name='films/movies_detail.html',
#                       context={'details': details})

#добавление
class CreateMoviesView(generic.CreateView):
    template_name = 'films/crud/create_film.html'
    form_class = forms.MoviesForm
    success_url = '/movies_list'
    queryset = models.Movies.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateMoviesView, self).form_valid(form=form)

# def create_new_film(request):
#     if request.method == 'POST':
#         form = forms.MoviesForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Успешно добавлено <a href="/movies_list/">На главную</a>')
#     else:
#         form = forms.MoviesForm()
#     return render(request, template_name='films/crud/create_film.html',
#                   context={'form': form})

#удаление
class DeleteMovieView(generic.DeleteView):
    template_name = 'films/crud/confirm_delete.html'
    success_url = '/movies_list'

    def get_object(self, queryset=None):
        movie_id = self.kwargs.get('id')
        return get_object_or_404(models.Movies, id=movie_id)

# def delete_film(request, id):
#     movie_id = get_object_or_404(models.Movies, id=id)
#     movie_id.delete()
#     return HttpResponse('Успешно удалено <a href="/movies_list/">На главную</a>')

class EditFilmView(generic.UpdateView):
    template_name = 'films/crud/edit_film.html'
    form_class = forms.MoviesForm
    success_url = '/movies_list'
    queryset = models.Movies.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(EditFilmView, self).form_valid(form=form)

    def get_object(self, **kwargs):
        person_id = self.kwargs.get('id')
        return get_object_or_404(models.Movies, id=person_id)

# def edit_film(request,id):
#     movie_id = get_object_or_404(models.Movies, id=id)
#     if request.method == 'POST':
#         form = forms.MoviesForm(instance=movie_id, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Успешно измененно <a href="/movies_list/">На главную</a>')
#     else:
#         form = forms.MoviesForm(instance=movie_id)
#     return render(request,
#             template_name='films/crud/edit_film.html',
#             context={'form':form,
#                      'movie_id':movie_id
#             })

class CreateMovieReviewView(generic.CreateView):
    template_name = 'films/crud/add_review.html'
    form_class = forms.ReviewForm
    success_url = '/movies_list/'
    queryset = models.Review.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateMovieReviewView, self).form_valid(form=form)

# def add_review(request):
#     if request.method == 'POST':
#         form = forms.ReviewForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Отзыв успешно добавлен <a href="/movies_list/">На главную</a>')
#     else:
#         form = forms.ReviewForm()
#     return render(request, template_name='films/crud/add_review.html',
#                   context={'form': form})

class SearchView(generic.ListView):
    template_name = 'films/movies_list.html'
    context_object_name = 'movies'
    paginate_by = '5'

    def get_queryset(self):
        return models.Movies.objects.filter(name__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context
