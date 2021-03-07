from django.shortcuts import render
from .models import *


def index_handler(request):
    categories = Category.objects.prefetch_related('parent_category').filter(order=1)
    schools = School.objects.all()
    course = Course.objects.all()
    context = {
        'categories': categories,
        'schools': schools,
        'course':course
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
        courses = Course.objects.filter(categories__slug=cat_slug).prefetch_related('categories', 'school', 'features',
                                                                                    'course_format')
        category = Category.objects.get(slug=cat_slug)
    else:
        courses = Course.objects.all().prefetch_related('categories', 'school', 'features', 'course_format')
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
    schools = School.objects.all()
    context = {
        'schools': schools,
    }
    return render(request, 'listing/schools.html', context)


def school_detail_handler(request, slug):
    school = School.objects.get(slug=slug)
    schools = School.objects.all()
    context = {
        'school': school,
        'schools': schools,
    }
    return render(request, 'listing/school-detail.html', context)


def robots_handler(request):
    context = {}
    return render(request, 'listing/robots.txt', context, content_type='text/plain')
