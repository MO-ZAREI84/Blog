# Generated by Django 5.0.7 on 2024-10-23 10:50

import django.db.models.deletion
import django.utils.timezone
import django_jalali.db.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloog', '0009_alter_ticket_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='ناریخ تولید'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=django_jalali.db.models.jDateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ انتشار'),
        ),
        migrations.AlterField(
            model_name='post',
            name='update',
            field=django_jalali.db.models.jDateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی'),
        ),
        migrations.CreateModel(
            name='ImageField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_file', models.ImageField(upload_to='post_images/')),
                ('title', models.CharField(blank=True, max_length=20, null=True, verbose_name='عنوان')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('create', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='ناریخ تولید')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='bloog.post', verbose_name='تصویر')),
            ],
        ),
    ]
