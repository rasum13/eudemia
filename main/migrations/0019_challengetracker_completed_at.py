# Generated by Django 5.1.5 on 2025-01-18 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0018_challengetracker_answer"),
    ]

    operations = [
        migrations.AddField(
            model_name="challengetracker",
            name="completed_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]