# Generated by Django 3.1.5 on 2021-01-25 08:03

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210121_1321'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='category',
            managers=[
                ('odjects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='comment',
            managers=[
                ('odjects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='newsletter',
            managers=[
                ('odjects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='post',
            managers=[
                ('odjects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='tag',
            managers=[
                ('odjects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
