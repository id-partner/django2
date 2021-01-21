# Generated by Django 3.1.5 on 2021-01-21 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210118_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Опубликованно?'),
        ),
        migrations.AlterField(
            model_name='category',
            name='in_menu',
            field=models.BooleanField(default=True, verbose_name='Добавляем в меню?'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название категории'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='Запись'),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активна подписка?'),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='subscription_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата подписки'),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='unsubscribe_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата отписки'),
        ),
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(to='blog.Category', verbose_name='Категории'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='Контент поста'),
        ),
        migrations.AlterField(
            model_name='post',
            name='main_image',
            field=models.ImageField(upload_to='images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Тайтл поста'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='post',
            name='short_description',
            field=models.TextField(verbose_name='Короткое описание'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag', verbose_name='Теги'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название тега'),
        ),
    ]
