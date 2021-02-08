from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from django.utils.html import format_html
from .models import *


def set_discount_status(modeladmin, request, queryset):
    for object in queryset:
        object.discount = True
        object.save()


set_discount_status.short_description = 'Проставить статус скидки всем курсам'


class CategoryAdmin(SummernoteModelAdmin):
    summernote_fields = ('content', 'description',)
    list_display = ('name', 'in_menu', 'order', 'parent', 'flaticon', 'course_count',)
    list_editable = ('in_menu', 'order', 'parent', 'flaticon',)
    search_fields = ('name',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('course_set')

    def course_count(self, object):
        return object.course_set.all().count()


class SchoolCourseInLine(admin.TabularInline):
    model = Course
    exclude = ('description', 'categories', '')


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('logo_code', 'name', 'link',)
    list_display_links = ('logo_code', 'name',)
    search_fields = ('name',)
    inlines = (SchoolCourseInLine,)

    def logo_code(self, object):
        return format_html('<img src="{}" style="max-width: 100px" />',
                           object.logo.url
                           )


class CourselAdmin(admin.ModelAdmin):
    list_display = ('name', 'school', 'start_date', 'price', 'discount',)
    list_filter = ('categories', 'school',)
    search_fields = ('name', 'school',)
    actions = (set_discount_status,)


admin.site.register(Category, CategoryAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Features)
admin.site.register(Course, CourselAdmin)
admin.site.register(Review)
admin.site.register(CourseFormat)
