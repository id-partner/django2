from listing.models import School, Category
from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class SchoolSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        return School.objects.all()


class CategorySitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return Category.objects.all()


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return ['about', 'contact', ]

    def location(self, item):
        return reverse(item)
