# Generated by Django 4.1.4 on 2023-01-27 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("takmedia", "0007_remove_blog_sous_titre"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="date",
            field=models.DateTimeField(),
        ),
    ]
