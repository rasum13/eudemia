# Generated by Django 5.1.5 on 2025-01-24 17:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0028_rename_shopitempurchase_purchase"),
        ("users", "0011_remove_student_completed_challenge_questions_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Attendance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                (
                    "status",
                    models.CharField(
                        choices=[("present", "Present"), ("absent", "Absent")],
                        max_length=10,
                    ),
                ),
                ("days_attended", models.PositiveIntegerField(default=0)),
                ("days_passed", models.PositiveIntegerField(default=60)),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.student"
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Attendence",
        ),
    ]
