# Generated by Django 5.0.2 on 2024-04-01 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp5', '0022_product_sub_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sub_category',
            field=models.CharField(choices=[('Men', 'Men'), ('Women', 'Women'), ('Kids', 'Kids'), ('Beauty', 'Beauty')], max_length=200),
        ),
    ]