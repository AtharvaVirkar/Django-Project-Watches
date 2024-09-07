# Generated by Django 5.0.4 on 2024-04-14 12:16

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("phone_number", models.CharField(max_length=20)),
                ("message", models.TextField()),
                ("date_created", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name_plural": "Contact Table",
            },
        ),
    ]
