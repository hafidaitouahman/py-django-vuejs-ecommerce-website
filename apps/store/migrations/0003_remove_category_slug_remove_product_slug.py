# Generated by Django 5.0.6 on 2024-06-28 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_category_options_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]
