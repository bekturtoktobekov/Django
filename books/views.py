from django.shortcuts import render
from . import models

def books_view(request):
    if request.method == 'GET':
        post = models.Books.objects.all()
        return render(request, template_name='books.html',
                      context={'post' : post})
