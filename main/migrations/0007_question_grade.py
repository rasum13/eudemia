# Generated by Django 5.1.4 on 2025-01-15 20:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0006_question_unit"),
        ("users", "0002_alter_student_blood_group"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="grade",
            field=models.ForeignKey(
                default=4, on_delete=django.db.models.deletion.CASCADE, to="users.class"
            ),
        ),
    ]
