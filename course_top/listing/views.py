from django.shortcuts import render


def index_handler(request):
    context = {}
    return render(request, 'listing/index.html', context)


def about_handler(request):
    context = {}
    return render(request, 'listing/about-us.html', context)


def contact_handler(request):
    context = {}
    return render(request, 'listing/contact.html', context)


def course_list_handler(request):
    context = {}
    return render(request, 'listing/course-list.html', context)


def course_detail_handler(request):
    context = {}
    return render(request, 'listing/course-detail.html', context)


def school_list_handler(request):
    context = {}
    return render(request, 'listing/teachers.html', context)


def school_detail_handler(request):
    context = {}
    return render(request, 'listing/teacher-detail.html', context)


def robots_handler(request):
    context = {}
    return render(request, 'listing/robots.txt', context, content_type='text/plain')
