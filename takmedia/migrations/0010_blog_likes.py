# Generated by Django 4.1.4 on 2023-01-30 11:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("takmedia", "0009_alter_blog_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="likes",
            field=models.ManyToManyField(
                blank=True, related_name="likes", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
