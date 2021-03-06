# Generated by Django 3.2 on 2021-04-08 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Item",
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
                ("title", models.TextField(max_length=150)),
                ("desc", models.TextField(max_length=300)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="item_images"),
                ),
                ("curent_sale", models.CharField(blank=True, max_length=150)),
                ("is_active", models.BooleanField(default=False)),
            ],
        ),
    ]
