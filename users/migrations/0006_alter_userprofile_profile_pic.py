# Generated by Django 5.1.5 on 2025-01-18 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_alter_student_completed_challenge_questions_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="profile_pic",
            field=models.ImageField(
                default="profile_pictures/profile.png", upload_to="profile_pictures/"
            ),
        ),
    ]
