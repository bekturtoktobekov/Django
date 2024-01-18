from django.shortcuts import render
from . import models

def blog_view(request):
    if request.method == 'GET':
        post = models.Blog.objects.all()
        return render(request, template_name='blog.html',
                      context={'post' : post})
