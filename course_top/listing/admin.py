from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *


class CategoryAdmin(SummernoteModelAdmin):  # Класс для HTML редактора для модели Пост
    summernote_fields = ('content', 'description')


admin.site.register(Category, CategoryAdmin)
admin.site.register(School)
admin.site.register(Features)
admin.site.register(Course)
admin.site.register(Review)
