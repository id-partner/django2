from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Category, Tag, Post, Comment, Newsletter

class PostAdmin(SummernoteModelAdmin): #Класс для HTML редактора для модели Пост
    summernote_fields = ('content','short_description')

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Newsletter)
