# Generated by Django 5.1.5 on 2025-01-16 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0012_quiz_quizquestion_quiz"),
        ("users", "0002_alter_student_blood_group"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="completed_challenge_questions",
            field=models.ManyToManyField(to="main.question"),
        ),
        migrations.AddField(
            model_name="student",
            name="completed_quiz_questions",
            field=models.ManyToManyField(to="main.quizquestion"),
        ),
    ]
