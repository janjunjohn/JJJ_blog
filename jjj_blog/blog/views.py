from django.shortcuts import render
from .models import Tag, Blog


def index(request):
    blogs = Blog.objects.all()
    tags = Tag.objects.all()

    params = {
        'posts': blogs,
        'tags': tags,
    }
    return render(request, 'blog/index.html', params)
