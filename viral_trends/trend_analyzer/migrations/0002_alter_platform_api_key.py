# Generated by Django 5.1.1 on 2024-09-10 18:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("trend_analyzer", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="platform",
            name="api_key",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
