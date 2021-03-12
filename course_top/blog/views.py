from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *


def blog_handler(request, **kwargs):
    cat_slug = kwargs.get('cat_slug')
    current_page = request.GET.get('page')
    posts_on_page = 5
    if cat_slug:
        category = Category.objects.get(slug=cat_slug)
        posts = Post.objects.filter(categories__slug=cat_slug).prefetch_related('categories')
        paginator = Paginator(posts, posts_on_page)
        page_obj = paginator.get_page(current_page)
    else:
        posts = Post.objects.all().prefetch_related('categories')
        category = None
        paginator = Paginator(posts, posts_on_page)
        page_obj = paginator.get_page(current_page)

    context = {
        # 'posts': posts,
        'category': category,
        'page_obj': page_obj,
        'paginator': paginator,
    }
    return render(request, 'blog/classic-full-width.html', context)


def single_blog_handler(request, slug):
    post = Post.objects.get(slug=slug)
    prev_post = Post.objects.filter(id=post.id - 1).first()
    next_post = Post.objects.filter(id=post.id + 1).first()
    context = {
        'post': post,
        'prev_post': prev_post,
        'next_post': next_post,
    }
    return render(request, 'blog/blog-single.html', context)
