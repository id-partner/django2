from django.db import models
from mptt.models import MPTTModel, TreeForeignKey,TreeManyToManyField

from django.urls import reverse


class SEOListing(models.Model):
    title = models.CharField(max_length=80, blank=True, null=True)
    seo_description = models.CharField(max_length=255, blank=True, null=True)
    canonical_url = models.URLField(blank=True, null=True)
    meta_robots = models.CharField(max_length=50, blank=True, null=True)
    h1 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        abstract = True


class Category(MPTTModel):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    slug = models.SlugField(max_length=255, unique=True)
    in_menu = models.BooleanField(default=True, verbose_name='Добавляем ли в меню?')
    order = models.IntegerField(default=1)
    description = models.CharField(max_length=255, blank=True, verbose_name='Описание')
    content = models.TextField(blank=True)
    icon = models.ImageField(upload_to='images/category/%Y/%m/%d/', blank=True, verbose_name='Иконка категории')
    flaticon = models.CharField(max_length=255, blank=True, null=True, verbose_name='Флэт-иконка')
    parent = TreeForeignKey(
        'self', on_delete=models.DO_NOTHING, null=True,
        blank=True, related_name='child_category',
        verbose_name='Родительская категория'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('course_list',  args=[self.slug],)


class School(SEOListing):
    name = models.CharField(max_length=255, verbose_name='Название школы')
    slug = models.SlugField(max_length=255, unique=True)
    description = models.CharField(max_length=255, blank=True, verbose_name='Описание')
    categories = models.ManyToManyField(Category, blank=True, verbose_name='Категория')
    logo = models.ImageField(upload_to='images/school/%Y/%m/%d/', blank=True, verbose_name='Логотип')
    link = models.URLField(blank=True, verbose_name='Ссылка на школу')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Школа'
        verbose_name_plural = 'Школы'

    def get_absolute_url(self):
        return reverse('school_detail', args=(self.slug, ))


class Features(models.Model):
    name = models.CharField(max_length=255, verbose_name='Особенности курса')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Особенность'
        verbose_name_plural = 'Особенности'


class CourseFormat(models.Model):
    name = models.CharField(max_length=255, verbose_name='Особенности курса')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Формат курса'
        verbose_name_plural = 'Форматы курсов'


class Course(SEOListing):
    name = models.CharField(max_length=255, verbose_name='Название курса')
    description = models.CharField(blank=True, max_length=255, verbose_name='Описание курса')
    categories = TreeManyToManyField(Category, verbose_name='Категория')
    link = models.URLField(verbose_name='Ссылка на страницу курса')
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='school_courses', verbose_name='Школа')
    price = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='Базовая стоимость')
    deferred_payment = models.BooleanField(default=True, verbose_name='Есть ли рассрочка?')
    discount = models.BooleanField(default=False, verbose_name='Есть ли скидка?')
    discount_amount = models.IntegerField(null=True, blank=True, verbose_name='Размер скидки')
    discounted_price = models.DecimalField(null=True, max_digits=19, decimal_places=2, blank=True,
                                           verbose_name='Стоимость по скидке')
    duration = models.CharField(max_length=255, verbose_name='Продолжительность')
    start_date = models.DateField(null=True, blank=True, verbose_name='Дата старта')
    features = models.ManyToManyField(Features, blank=True, verbose_name='Особенности')
    course_format = models.ManyToManyField(CourseFormat, blank=True, verbose_name='Формат курса')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Добавлен')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлен')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Review(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(verbose_name='Почта')
    source = models.CharField(max_length=255, verbose_name='Источник', blank=True, null=True)
    head = models.CharField(max_length=255, verbose_name='Заголовок', blank=True, null=True)
    comment = models.TextField(verbose_name='Комментарий')
    positive = models.TextField(blank=True, null=True, verbose_name='Плюсы')
    negative = models.TextField(blank=True, null=True, verbose_name='Минусы')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации', blank=True, null=True)
    rating = models.FloatField(verbose_name='Рейтинг', blank=True, null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, verbose_name='Школа')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', blank=True, null=True )
    is_published = models.BooleanField(default=False, verbose_name='Опубликовать')

    def __str__(self):
        return self.comment[:20]

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
