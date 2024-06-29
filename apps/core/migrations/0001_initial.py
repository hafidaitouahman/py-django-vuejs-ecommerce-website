# Generated by Django 5.0.6 on 2024-06-28 18:41

import logging
import environ
from django.db import migrations

logger = logging.getLogger(__name__)

def generate_superuser(apps, schema_editor):
    from django.contrib.auth import get_user_model

    env = environ.Env()
    USERNAME = env.str("ADMIN_USERNAME")
    PASSWORD = env.str("ADMIN_PASSWORD")
    EMAIL = env.str("ADMIN_EMAIL")

    user = get_user_model()

    if not user.objects.filter(username=USERNAME, email=EMAIL).exists():
        logger.info("Creating new superuser")
        admin = user.objects.create_superuser(
           username=USERNAME, password=PASSWORD, email=EMAIL
        )
        admin.save()
    else:
        logger.info("Superuser already created!")


class Migration(migrations.Migration):
    #dependencies = [("core", "0009_user_full_name")
    #]
    operations = [migrations.RunPython(generate_superuser)
    ]
