# Generated by Django 3.2 on 2021-04-08 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("items", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="title",
            field=models.CharField(max_length=150),
        ),
    ]
