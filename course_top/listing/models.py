from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    in_menu = models.BooleanField(default=True)
    order = models.IntegerField(default=1)
