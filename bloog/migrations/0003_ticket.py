# Generated by Django 5.0.7 on 2024-10-11 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloog', '0002_alter_post_options_alter_post_author_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='پیام')),
                ('name', models.CharField(max_length=250, verbose_name=' نام')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('phone', models.IntegerField(verbose_name='شماره')),
                ('subjects', models.CharField(max_length=240, verbose_name='موضوع')),
            ],
        ),
    ]
