# Generated by Django 3.1.5 on 2021-01-26 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0007_auto_20210125_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.ImageField(blank=True, upload_to='images/category/%Y/%m/%d/', verbose_name='Иконка категории'),
        ),
        migrations.AlterField(
            model_name='course',
            name='discounted_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19, verbose_name='Стоимость по скидке'),
        ),
        migrations.AlterField(
            model_name='course',
            name='link',
            field=models.URLField(verbose_name='Ссылка на страницу курса'),
        ),
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=19, verbose_name='Базовая стоимость'),
        ),
        migrations.AlterField(
            model_name='school',
            name='link',
            field=models.URLField(verbose_name='Ссылка на школу'),
        ),
        migrations.AlterField(
            model_name='school',
            name='logo',
            field=models.ImageField(upload_to='images/school/%Y/%m/%d/', verbose_name='Логотип'),
        ),
    ]