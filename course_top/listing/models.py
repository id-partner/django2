from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    slug = models.SlugField(max_length=255)
    in_menu = models.BooleanField(default=True, verbose_name='Добавляем ли в меню?')
    order = models.IntegerField(default=1)
    description = models.CharField(max_length=255, verbose_name='Описание')
    content = models.TextField(blank=True)
    icon = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True, verbose_name='Иконка категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class SubCategory(models.Model):
    parent_category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Родительская категория')
    name = models.CharField(max_length=255, verbose_name='Название подкатегории')
    slug = models.SlugField(max_length=255)
    in_menu = models.BooleanField(default=True, verbose_name='Добавляем ли в меню?')
    order = models.IntegerField(default=1)
    content = models.TextField(blank=True)
    description = models.CharField(max_length=255, verbose_name='Описание')
    icon = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True, verbose_name='Иконка подкатегории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class School(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название школы')
    slug = models.SlugField(max_length=255)
    description = models.CharField(max_length=255, verbose_name='Описание')
    categories = models.ManyToManyField(Category, verbose_name='Категория')
    subcategories = models.ManyToManyField(SubCategory, verbose_name='Подкатегория')
    logo = models.ImageField(upload_to='images/%Y/%m/%d/', verbose_name='Логотип')
    link = models.CharField(max_length=255, verbose_name='Ссылка на школу')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Школы'
        verbose_name_plural = 'Школа'


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


class Course(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название курса')
    description = models.CharField(max_length=255, verbose_name='Описание курса')
    categories = models.ManyToManyField(Category, verbose_name='Категория')
    subcategories = models.ManyToManyField(SubCategory, blank=True, verbose_name='Подкатегория')
    link = models.CharField(max_length=255, verbose_name='Ссылка на страницу курса')
    school = models.ForeignKey(School, on_delete=models.CASCADE, verbose_name='Школа')
    price = models.IntegerField(verbose_name='Базовая стоимость')
    deferred_payment = models.BooleanField(default=True, verbose_name='Есть ли рассрочка?')
    discount = models.BooleanField(default=False, verbose_name='Есть ли скидка?')
    discount_amount = models.IntegerField(blank=True, verbose_name='Размер скидки')
    discounted_price = models.IntegerField(verbose_name='Стоимость по скидке')
    duration = models.CharField(max_length=255, verbose_name='Продолжительность')
    start_date = models.DateField(blank=True, verbose_name='Дата старта')
    features = models.ManyToManyField(Features, verbose_name='Особенности')
    course_format = models.ManyToManyField(CourseFormat, verbose_name='Формат курса')
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
    comment = models.TextField(verbose_name='Комментарий')
    rating = models.FloatField(verbose_name='Рейтинг')
    school = models.ForeignKey(School, on_delete=models.CASCADE, verbose_name='Школа')

    def __str__(self):
        return self.comment[:20]

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'