from django.shortcuts import render, get_object_or_404
from . import models

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
