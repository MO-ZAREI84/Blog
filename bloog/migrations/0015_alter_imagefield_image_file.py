# Generated by Django 5.0.7 on 2024-10-24 13:02

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloog', '0014_alter_imagefield_options_alter_imagefield_create_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagefield',
            name='image_file',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=-1, scale=None, size=[500, 500], upload_to='post_images/'),
        ),
    ]
