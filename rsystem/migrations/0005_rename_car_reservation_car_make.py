# Generated by Django 4.2.7 on 2023-12-20 16:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("rsystem", "0004_reservation"),
    ]

    operations = [
        migrations.RenameField(
            model_name="reservation",
            old_name="car",
            new_name="car_make",
        ),
    ]
