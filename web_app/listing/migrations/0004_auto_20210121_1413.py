# Generated by Django 3.1.5 on 2021-01-21 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0003_auto_20210121_1329'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.RemoveField(
            model_name='course',
            name='subcategories',
        ),
        migrations.RemoveField(
            model_name='school',
            name='subcategories',
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='parent_category', to='listing.category'),
        ),
        migrations.AlterField(
            model_name='course',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='school_courses', to='listing.school', verbose_name='Школа'),
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
    ]
