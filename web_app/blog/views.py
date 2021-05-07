from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *
from django.views.generic import ListView, DetailView


class BlogListView(ListView):
    template_name = 'blog/classic-full-width.html'
    model = Post
    ordering = '-pub_date'
    paginate_by = 3

    def get_queryset(self):
        self.cat_slug = self.kwargs.get('cat_slug')
        qs = super().get_queryset()
        if self.cat_slug:
            qs = qs.filter(categories__slug=self.cat_slug)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.cat_slug:
            context['category'] = Category.objects.get(slug=self.cat_slug)
        return context


class SinglePost(DetailView):
    template_name = 'blog/blog-single.html'
    model = Post
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prev_post']=Post.objects.filter(id=self.object.id - 1).first()
        context['next_post'] = Post.objects.filter(id=self.object.id + 1).first()
        return context


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


