# Generated by Django 3.1.5 on 2021-04-09 10:29

from django.db import migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0015_auto_20210409_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='categories',
            field=mptt.fields.TreeManyToManyField(to='listing.Category', verbose_name='Категория'),
        ),
    ]
