# Generated by Django 3.1.5 on 2021-06-26 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0025_auto_20210626_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='link',
            field=models.CharField(blank=True, max_length=255, verbose_name='Ссылка на школу'),
        ),
    ]
