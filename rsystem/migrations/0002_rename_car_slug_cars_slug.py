# Generated by Django 4.2.7 on 2023-12-18 16:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("rsystem", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cars",
            old_name="car_slug",
            new_name="slug",
        ),
    ]
