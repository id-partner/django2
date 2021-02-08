from django.shortcuts import render
from .models import *


def index_handler(request):
    categories = Category.objects.filter(order=1)
    schools = School.objects.all()
    courses = Course.objects.all()
    context = {
        'categories': categories,
        'schools': schools,
        'courses': courses,
    }
    return render(request, 'listing/index.html', context)


def about_handler(request):
    context = {}
    return render(request, 'listing/about-us.html', context)


def contact_handler(request):
    context = {}
    return render(request, 'listing/contact.html', context)


def course_list_handler(request, slug):
    context = {}
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
