# Generated by Django 5.1.5 on 2025-01-18 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0015_challengetracker_completed_questions"),
    ]

    operations = [
        migrations.RenameField(
            model_name="challengetracker",
            old_name="completed_questions",
            new_name="correct_questions",
        ),
    ]
