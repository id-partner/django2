from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    slug = models.SlugField(max_length=255)
    in_menu = models.BooleanField(default=True, verbose_name='Добавляем в меню?')
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название тега')
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Post(models.Model):
    name = models.CharField(max_length=255, verbose_name='Тайтл поста')
    slug = models.SlugField(max_length=255)
    content = models.TextField(verbose_name='Контент поста')
    short_description = models.TextField(verbose_name='Короткое описание')
    main_image = models.ImageField(upload_to='images/%Y/%m/%d/')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    categories = models.ManyToManyField(Category, verbose_name='Категории')
    tags = models.ManyToManyField(Tag, verbose_name='Теги')
    is_published = models.BooleanField(default=False, verbose_name='Опубликованно?')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comment(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(verbose_name='Почта')
    comment = models.TextField(verbose_name='Комментарий')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Запись')

    def __str__(self):
        return self.comment[:20]

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Newsletter(models.Model):
    email = models.EmailField(verbose_name='Почта')
    is_active = models.BooleanField(default=True, verbose_name='Активна подписка?')
    subscription_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата подписки')
    unsubscribe_date = models.DateTimeField(null=True, blank=True, verbose_name='Дата отписки')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Подписка на почту'
        verbose_name_plural = 'Подписки на почту'
