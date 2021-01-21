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

from polls.views import detail
from listing.views import *  # импортируем вьюхи из приложения листинга
from blog import views  # импортируем вьюхи из приложения блога

urlpatterns = [
                  path('', index_handler),
                  path('polls/<int:question_id>/', detail),
                  path('blog/', views.blog_handler),
                  path('single_blog/', views.single_blog_handler),
                  path('about/', about_handler),
                  path('contact/', contact_handler),
                  path('course_list/', course_list_handler),
                  path('school/', school_list_handler),
                  path('course_detail/', course_detail_handler),
                  path('school_detail/', school_detail_handler),
                  path('robots.txt', robots_handler),
                  path('admin/', admin.site.urls),
                  path('summernote/', include('django_summernote.urls')),
                  # path('__debug__/', include(debug_toolbar.urls)),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls)),]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
