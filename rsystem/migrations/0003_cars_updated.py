# Generated by Django 4.2.7 on 2023-12-19 16:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rsystem", "0002_rename_car_slug_cars_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="cars",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
