# Generated by Django 4.0.3 on 2022-03-26 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Config",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("token", models.CharField(max_length=80)),
                ("url", models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
