# Generated by Django 3.2 on 2021-04-09 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("items", "0003_auto_20210409_1019"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="is_top_item",
            field=models.BooleanField(default=False),
        ),
    ]
