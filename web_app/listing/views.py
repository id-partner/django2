from django.shortcuts import render
from .models import *

from .forms import ReviewForm
from django.contrib import messages
from django.views.generic.edit import FormMixin

from django.urls import reverse
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, DetailView

from django.db.models import Avg, Sum, Min, Max, Count, Q
from django.contrib.postgres.search import SearchVector
from django.core.paginator import Paginator


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

    # paginate_by = 20

    def get_queryset(self):
        qs = super().get_queryset().annotate(Avg_rating=Avg(
            'school__review__rating')).prefetch_related('categories',
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
                                                                                ).select_related(
                    'school').order_by('-name')

            else:
                qs = qs.filter(categories__slug=self.cat_slug).prefetch_related('categories',
                                                                                'features',
                                                                                'course_format',
                                                                                ).select_related(
                    'school').order_by('-name')

        # TODO: получение списка курсов по указанной школе в фильтре доработать
        if self.request.GET.getlist('school'):
            school = self.request.GET.getlist('school')
            qs = qs.filter(school__name__in=school)
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['schools_name'] = School.objects.all().values('name', 'id').distinct()

        if len(self.request.GET.getlist('school')) == 1:
            context['schools_name'] = School.objects.filter(
                school_courses__in=self.object_list).values('name', 'id').distinct()

        if self.cat_slug:
            context['category'] = Category.objects.get(slug=self.cat_slug)
            context['schools_name'] = School.objects.filter(
                school_courses__in=self.object_list).values('name', 'id').distinct()
        return context


def course_detail_handler(request):
    context = {}
    return render(request, 'listing/course-detail.html', context)


class SchoolListView(ListView):
    template_name = 'listing/schools.html'
    context_object_name = 'schools'
    paginate_by = 10

    def get_queryset(self):
        return School.objects.annotate(Avg_rating=Avg('review__rating')).prefetch_related(
            'review_set', ).order_by('-name')


class SchoolDetailView(FormMixin, DetailView):
    template_name = 'listing/school-detail.html'
    model = School
    slug_url_kwarg = 'slug'
    form_class = ReviewForm

    def get_context_data(self, **kwargs):
        review = Review.objects.filter(
            school__slug=self.kwargs.get('slug')).values('rating')

        course = Course.objects.filter(
            school__slug=self.kwargs.get('slug'))

        context = super().get_context_data(**kwargs)
        context['schools'] = School.objects.all()

        context['course'] = course.aggregate(
            Avg_price=Avg('price'),
            Max_price=Max('price'),
            Min_price=Min('price'),

        )

        context['rating'] = review.aggregate(
            Cnt=Count('rating'),
            Avg=Avg('rating'),
            Min=Min('rating'),
            Max=Max('rating'),
            Cnt_star1=Count('rating', filter=Q(rating__lt=1.5)),
            Cnt_star2=Count('rating', filter=Q(rating__gte=1.5, rating__lt=2.5)),
            Cnt_star3=Count('rating', filter=Q(rating__gte=2.5, rating__lt=3.5)),
            Cnt_star4=Count('rating', filter=Q(rating__gte=3.5, rating__lt=4.5)),
            Cnt_star5=Count('rating', filter=Q(rating__gte=4.5))
        )
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


class SearchView(ListView):
    template_name = 'listing/search.html'
    context_object_name = 'courses'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        self.query = self.request.GET.get('q')
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return Course.objects.annotate(
            search=SearchVector('name', 'description'),
            Avg_rating=Avg('school__review__rating'),
        ).prefetch_related('categories',
                           'features',
                           'course_format',
                           ).select_related('school').filter(search=self.query)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['query'] = self.query
        context['cnt_courses'] = Course.objects.annotate(
            search=SearchVector('name', 'description'),
        ).filter(search=self.query).count()

        return context
