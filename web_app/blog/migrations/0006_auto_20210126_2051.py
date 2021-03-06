# Generated by Django 3.1.5 on 2021-01-26 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210125_1307'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='category',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='comment',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='newsletter',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='post',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='tag',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='main_image',
            field=models.ImageField(upload_to='images/post/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='short_description',
            field=models.CharField(max_length=255, verbose_name='Короткое описание'),
        ),
    ]
