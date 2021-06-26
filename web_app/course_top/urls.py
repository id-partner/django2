"""course_top URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar

from django.contrib.sitemaps.views import sitemap, index

from listing.views import *  # импортируем вьюхи из приложения листинга
from blog import views  # импортируем вьюхи из приложения блога

from listing.sitemap import *

from django.views.decorators.cache import cache_page

sitemaps = {
    'schools': SchoolSitemap,
    'categories': CategorySitemap,
    'static': StaticViewSitemap,
    'schools-courses': SchoolCoursesSitemap,
    'schools-courses-categories': SchoolCoursesCategoriesSitemap
}


urlpatterns = [
                  path('', cache_page(60*60)(IndexView.as_view()), name='homepage'),
                  # path('blog/', views.BlogListView.as_view(), name='blog'),
                  # path('blog/<cat_slug>', views.BlogListView.as_view(), name='blog_category'),
                  # path('single_blog/<slug>', views.SinglePost.as_view(), name='single_blog'),

                  path('search/', SearchView.as_view(), name='search'),

                  path('courses/', cache_page(60*60)(CourseListView.as_view()), name='course_list'),
                  path('courses/<cat_slug>', cache_page(60*60)(CourseListView.as_view()), name='course_list_category'),

                  path('school_courses/<school_slug>', cache_page(60*60)(
                      CourseListSchoolView.as_view()), name='course_list_school'),
                  path('school_courses/<cat_slug>/<school_slug>', cache_page(60*60)(CourseListSchoolView.as_view()),
                       name='course_list_category_school'),

                  path('about/', AboutView.as_view(), name='about'),
                  path('contact/', ContactView.as_view(), name='contact'),
                  path('robots.txt', RobotsView.as_view(), name='robots'),

                  path('sitemap.xml', index, {'sitemaps': sitemaps}),
                  path('sitemap-<section>.xml', cache_page(86400)(sitemap), {'sitemaps': sitemaps},
                       name='django.contrib.sitemaps.views.sitemap'),

                  path('admin/', admin.site.urls),
                  path('summernote/', include('django_summernote.urls')),

                  path('schools/', cache_page(60*60)(SchoolListView.as_view()), name='school'),
                  path('<school_slug>/', cache_page(60*60)(SchoolDetailView.as_view()), name='school_detail'),
                  # path('course_detail/', course_detail_handler, name='course_detail'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls)), ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
