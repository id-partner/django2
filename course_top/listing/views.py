from django.shortcuts import render
from .models import *

from .forms import ReviewForm
from django.contrib import messages
from django.views.generic.edit import FormMixin

from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView

from django.db.models import Avg, Sum, Min, Max, Count
from django.db.models import Func


class IndexView(TemplateView):
    template_name = 'listing/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.prefetch_related('course_set', 'child_category').filter(order=1)
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
    context_object_name = 'courses'

    def get_queryset(self):
        qs = super().get_queryset().prefetch_related('categories',
                                                     'features',
                                                     'course_format',
                                                     ).select_related('school')
        self.cat_slug = self.kwargs.get('cat_slug')

        if self.cat_slug:
            category = Category.objects.get(slug=self.cat_slug)
            if category.child_category.all().count() > 0:
                slug_list = category.child_category.all().values_list('slug')
                qs = qs.filter(categories__slug__in=slug_list).prefetch_related('categories',
                                                                                'features',
                                                                                'course_format',
                                                                                ).select_related('school')
            else:
                qs = qs.filter(categories__slug=self.cat_slug).prefetch_related('categories',
                                                                                'features',
                                                                                'course_format',
                                                                                ).select_related('school')

        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.cat_slug:
            context['category'] = Category.objects.get(slug=self.cat_slug)
        return context


def course_detail_handler(request):
    context = {}
    return render(request, 'listing/course-detail.html', context)


class SchoolListView(ListView):
    template_name = 'listing/schools.html'
    context_object_name = 'schools'

    def get_queryset(self):
        return School.objects.all().prefetch_related('review_set', )


class SchoolDetailView(FormMixin, DetailView):
    template_name = 'listing/school-detail.html'
    model = School
    slug_url_kwarg = 'slug'
    form_class = ReviewForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['schools'] = School.objects.all()
        context['rating'] = Review.objects.all().filter(
            school__slug=self.kwargs.get('slug')).aggregate(
            Avg=Avg('rating'), Min=Min('rating'), Max=Max('rating'))
        return context

    def get_success_url(self):
        return reverse('homepage')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        data = form.cleaned_data
        data['school'] = self.object
        Review.objects.create(**data)
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.add_message(
            self.request, messages.INFO,
            'Форма заполнена не корректно')
        return super().form_invalid(form)


class RobotsView(TemplateView):
    template_name = 'listing/robots.txt'
    content_type = 'text/plain'
