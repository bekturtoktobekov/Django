from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.http import HttpResponse

def movies_list(request):
    if request.method == 'GET':
        movies = models.Movies.objects.all()
        return render(request, template_name='films/movies_list.html',
                      context={'movies' : movies})
#
def movies_detail(request, id):
    if request.method == 'GET':
        details = get_object_or_404(models.Movies, id=id)
        return render(request, template_name='films/movies_detail.html',
                      context={'details': details})

#добавление
def create_new_film(request):
    if request.method == 'POST':
        form = forms.MoviesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Успешно добавлено <a href="/movies_list/">На главную</a>')
    else:
        form = forms.MoviesForm()
    return render(request, template_name='films/crud/create_film.html',
                  context={'form': form})

#удаление
def delete_film(request, id):
    movie_id = get_object_or_404(models.Movies, id=id)
    movie_id.delete()
    return HttpResponse('Успешно удалено <a href="/movies_list/">На главную</a>')

def edit_film(request,id):
    movie_id = get_object_or_404(models.Movies, id=id)
    if request.method == 'POST':
        form = forms.MoviesForm(instance=movie_id, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Успешно измененно <a href="/movies_list/">На главную</a>')
    else:
        form = forms.MoviesForm(instance=movie_id)
    return render(request,
            template_name='films/crud/edit_film.html',
            context={'form':form,
                     'movie_id':movie_id
            })

def add_review(request):
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Отзыв успешно добавлен <a href="/movies_list/">На главную</a>')
    else:
        form = forms.ReviewForm()
    return render(request, template_name='films/crud/add_review.html',
                  context={'form': form})