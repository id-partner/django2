from django.shortcuts import render
from .models import *


def index_handler(request):
    categories = Category.objects.filter(order=1)
    schools = School.objects.all()
    context = {
        'categories': categories,
        'schools': schools,
    }
    return render(request, 'listing/index.html', context)


def about_handler(request):
    context = {}
    return render(request, 'listing/about-us.html', context)


def contact_handler(request):
    context = {}
    return render(request, 'listing/contact.html', context)


def course_list_handler(request, **kwargs):
    cat_slug = kwargs.get('cat_slug')
    if cat_slug:
        courses = Course.objects.filter(categories__slug=cat_slug).prefetch_related('categories', 'school')
        category = Category.objects.get(slug=cat_slug)
    else:
        courses = Course.objects.all().prefetch_related('categories', 'school')
        category = None

    context = {
        'courses': courses,
        'category': category,
    }
    return render(request, 'listing/course-list.html', context)


def course_detail_handler(request):
    context = {}
    return render(request, 'listing/course-detail.html', context)


def school_list_handler(request):
    context = {}
    return render(request, 'listing/teachers.html', context)


def school_detail_handler(request, slug):
    context = {}
    return render(request, 'listing/teacher-detail.html', context)


def robots_handler(request):
    context = {}
    return render(request, 'listing/robots.txt', context, content_type='text/plain')
