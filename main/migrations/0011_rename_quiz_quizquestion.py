# Generated by Django 5.1.5 on 2025-01-16 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0010_question_challenge"),
        ("users", "0002_alter_student_blood_group"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Quiz",
            new_name="QuizQuestion",
        ),
    ]