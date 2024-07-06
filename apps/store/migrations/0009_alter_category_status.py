# Generated by Django 5.0.6 on 2024-06-29 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_category_status_alter_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='status',
            field=models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Iactive')], default='', max_length=2, null=True),
            preserve_default=False,
        ),
    ]
