# Generated by Django 3.1.5 on 2021-02-03 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0012_auto_20210129_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='flaticon',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Флэт-иконка'),
        ),
    ]
