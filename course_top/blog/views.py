from django.shortcuts import render
from .models import *


def blog_handler(request):
    posts = Post.objects.all().prefetch_related('categories')
    context = {
        'posts': posts
    }
    return render(request, 'blog/classic-full-width.html', context)


def single_blog_handler(request, slug):
    context = {}
    return render(request, 'blog/blog-single.html', context)


def blog_category_handler(request, slug):
    posts = Post.objects.all().prefetch_related('categories')
    context = {
        'posts': posts
    }
    return render(request, 'blog/classic-full-width.html', context)
