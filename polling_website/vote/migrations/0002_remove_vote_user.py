# Generated by Django 5.0.7 on 2024-08-04 11:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("vote", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="vote",
            name="user",
        ),
    ]