from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from django.utils.html import format_html
from .models import *


class CommentPostInLine(admin.TabularInline):
    model = Comment


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content', 'short_description')
    list_display = ('name', 'is_published', 'pub_date', 'image_code',)
    list_filter = ('is_published', 'pub_date', 'categories',)
    list_editable = ('is_published',)
    search_fields = ('name',)
    inlines = (CommentPostInLine,)

    def image_code(self, object):
        return format_html('<img src="{}" style="max-width: 50px" />',
                           object.main_image.url
                           )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'in_menu', 'order', 'posts_count')
    list_filter = ('in_menu', 'order',)
    search_fields = ('name',)
    list_editable = ('order',)
    readonly_fields = ('order',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('post_set')

    def posts_count(self, object):
        return object.post_set.all().count()


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'posts_count',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('post_set')

    def posts_count(self, object):
        return object.post_set.all().count()


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Newsletter)
