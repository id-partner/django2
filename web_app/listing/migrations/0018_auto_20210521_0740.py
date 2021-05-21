# Generated by Django 3.1.5 on 2021-05-21 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0017_auto_20210518_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='listing.course', verbose_name='Курс'),
        ),
        migrations.AddField(
            model_name='review',
            name='head',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='review',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Опубликованно?'),
        ),
        migrations.AddField(
            model_name='review',
            name='negative',
            field=models.TextField(blank=True, null=True, verbose_name='Минусы'),
        ),
        migrations.AddField(
            model_name='review',
            name='positive',
            field=models.TextField(blank=True, null=True, verbose_name='Плюсы'),
        ),
        migrations.AddField(
            model_name='review',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата публикации'),
        ),
        migrations.AddField(
            model_name='review',
            name='source',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Источник'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.FloatField(blank=True, null=True, verbose_name='Рейтинг'),
        ),
    ]
