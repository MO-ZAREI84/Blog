# Generated by Django 5.0.7 on 2024-10-18 10:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloog', '0007_post_reading_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='ناریخ تولید'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ انتشار'),
        ),
        migrations.AlterField(
            model_name='post',
            name='create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='ناریخ تولید'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ انتشار'),
        ),
        migrations.AlterField(
            model_name='post',
            name='update',
            field=models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی'),
        ),
    ]
