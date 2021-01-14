from django.shortcuts import render


def blog_handler(request):
    context = {}
    return render(request, 'blog/classic-full-width.html', context)


def single_blog_handler(request):
    context = {}
    return render(request, 'blog/blog-single.html', context)
