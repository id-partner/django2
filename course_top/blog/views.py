from django.shortcuts import render
from .models import *


def blog_handler(request):
    posts = Post.objects.all().prefetch_related('categories')
    context = {
        'posts': posts
    }
    return render(request, 'blog/classic-full-width.html', context)


def single_blog_handler(request, slug):
    post = Post.objects.get(slug=slug)
    prev_post = Post.objects.filter(id=post.id-1).first()
    next_post = Post.objects.filter(id=post.id+1).first()
    context = {
        'post': post,
        'prev_post':prev_post,
        'next_post':next_post,
    }
    return render(request, 'blog/blog-single.html', context)


def blog_category_handler(request, cat_slug):
    category = Category.objects.get(slug=cat_slug)
    posts = Post.objects.filter(categories__slug=cat_slug).prefetch_related('categories')
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'blog/classic-full-width.html', context)
