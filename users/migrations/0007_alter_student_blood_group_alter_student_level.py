# Generated by Django 5.1.5 on 2025-01-20 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_alter_userprofile_profile_pic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="blood_group",
            field=models.CharField(
                blank=True,
                choices=[
                    ("A+", "A+"),
                    ("A-", "A-"),
                    ("B+", "B+"),
                    ("B-", "B-"),
                    ("AB+", "AB+"),
                    ("AB-", "AB-"),
                    ("O+", "O+"),
                    ("O-", "O-"),
                ],
                max_length=10,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="level",
            field=models.PositiveIntegerField(default=1),
        ),
    ]