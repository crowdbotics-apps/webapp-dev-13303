# Generated by Django 2.2.16 on 2020-10-14 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_auto_20201014_1058"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customtext",
            name="title",
        ),
        migrations.AddField(
            model_name="customtext",
            name="titles",
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
