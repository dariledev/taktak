# Generated by Django 4.1.4 on 2023-01-27 20:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("takmedia", "0008_alter_blog_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="date",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
