# Generated by Django 5.0.2 on 2024-03-22 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp5', '0012_registration_adress_registration_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
