from django.shortcuts import render
from .models import *

from .forms import ReviewForm
from django.contrib import messages
from django.views.generic.edit import FormMixin

from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Q


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
        qs1 = super().get_queryset().prefetch_related('categories',
                                                     'features',
                                                     'course_format',
                                                     ).select_related('school')
        self.cat_slug = self.kwargs.get('cat_slug')

        if self.cat_slug:
            qs = qs1.filter(categories__slug=self.cat_slug).prefetch_related('categories',
                                                                            'features',
                                                                            'course_format',
                                                                            ).select_related('school')
            """вывод всех курсов дочерних категорий"""
            # if qs.count() < 1:
            #     category = Category.objects.filter(Q(parent=Category.objects.get(slug=self.cat_slug)))
            #     print(category)
            #     qs = qs1.filter(Q(categories=category[0])|Q(categories=category[1])|Q(categories=category[2]))
            #     print(qs)

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
            self.request, messages.INFO, 'Форма заполнена не корректно')
        return super().form_invalid(form)


class RobotsView(TemplateView):
    template_name = 'listing/robots.txt'
    content_type = 'text/plain'
