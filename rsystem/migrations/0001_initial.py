# Generated by Django 4.2.7 on 2023-12-14 14:01

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cars",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("car_make", models.CharField(max_length=100)),
                ("car_slug", models.SlugField(max_length=100)),
                ("car_model", models.IntegerField()),
                ("car_description", models.TextField()),
                ("car_rent", models.IntegerField()),
                ("car_image", models.ImageField(blank=True, upload_to="media")),
            ],
            options={
                "ordering": ["car_make"],
            },
        ),
    ]
