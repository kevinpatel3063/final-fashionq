# Generated by Django 4.2.4 on 2023-10-31 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp5', '0002_main_category_sub_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='main_category',
            name='img',
        ),
    ]
