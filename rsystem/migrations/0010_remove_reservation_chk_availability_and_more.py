# Generated by Django 4.2.7 on 2024-07-18 23:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rsystem", "0009_alter_reservation_start_time"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="reservation",
            name="chk_availability",
        ),
        migrations.AlterField(
            model_name="reservation",
            name="end_time",
            field=models.DateField(
                default=datetime.datetime(2024, 7, 19, 4, 8, 56, 969044)
            ),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="start_time",
            field=models.DateField(
                default=datetime.datetime(2024, 7, 19, 4, 8, 56, 969044)
            ),
        ),
    ]
