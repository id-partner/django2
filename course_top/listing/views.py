from django.shortcuts import render
from .models import *
from .forms import ReviewForm
from django.contrib import messages
from django.views.generic import TemplateView, ListView


class IndexView(TemplateView):
    template_name = 'listing/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.prefetch_related('parent_category').filter(order=1)
        context['schools'] = School.objects.all()
        context['course'] = Course.objects.all()
        return context


class AboutView(TemplateView):
    template_name = 'listing/about-us.html'


class ContactView(TemplateView):
    template_name = 'listing/contact.html'


class CourseListView(ListView):
    template_name = 'listing/course-list.html'
    model = Course

    def get_queryset(self):
        self.cat_slug = self.kwargs.get('cat_slug')
        qs = super().get_queryset()
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.cat_slug:
            context['courses'] = Course.objects.filter(categories__slug=self.cat_slug)
            context['categories'] = Category.objects.get(slug=self.cat_slug)
        else:
            context['courses'] = Course.objects.all().prefetch_related(
                'categories', 'school', 'features', 'course_format')
            context['categories'] = None


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


class SchoolListView(ListView):
    template_name = 'listing/schools.html'
    model = School

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['schools'] = School.objects.all().prefetch_related('review_set',)
        return context


def school_list_handler(request):
    schools = School.objects.all().prefetch_related('review_set',)
    context = {
        'schools': schools,
    }
    return render(request, 'listing/schools.html', context)


def school_detail_handler(request, slug):
    main_school = School.objects.get(slug=slug)
    school = School.objects.get(slug=slug)
    schools = School.objects.all()
    context = {
        'school': school,
        'schools': schools,
    }

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data['school'] = main_school
            Review.objects.create(**data)
            form = ReviewForm()
        else:
            messages.add_message(
                request, messages.INFO, 'Форма заполнена не корректно')
    else:
        form = ReviewForm()

    context['form'] = form

    return render(request, 'listing/school-detail.html', context)


class RobotsView(TemplateView):
    template_name = 'listing/robots.txt'
    content_type = 'text/plain'
