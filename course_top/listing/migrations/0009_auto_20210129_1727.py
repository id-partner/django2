# Generated by Django 3.1.5 on 2021-01-29 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0008_auto_20210126_2051'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='school',
            options={'verbose_name': 'Школа', 'verbose_name_plural': 'Школы'},
        ),
        migrations.AlterField(
            model_name='course',
            name='course_format',
            field=models.ManyToManyField(blank=True, to='listing.CourseFormat', verbose_name='Формат курса'),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.CharField(blank=True, max_length=255, verbose_name='Описание курса'),
        ),
        migrations.AlterField(
            model_name='course',
            name='features',
            field=models.ManyToManyField(blank=True, to='listing.Features', verbose_name='Особенности'),
        ),
        migrations.AlterField(
            model_name='school',
            name='categories',
            field=models.ManyToManyField(blank=True, to='listing.Category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='school',
            name='description',
            field=models.CharField(blank=True, max_length=255, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='school',
            name='link',
            field=models.URLField(blank=True, verbose_name='Ссылка на школу'),
        ),
        migrations.AlterField(
            model_name='school',
            name='logo',
            field=models.ImageField(blank=True, upload_to='images/school/%Y/%m/%d/', verbose_name='Логотип'),
        ),
    ]
