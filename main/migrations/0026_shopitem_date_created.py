# Generated by Django 5.1.5 on 2025-01-20 16:50

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0025_alter_shopitem_item_type_alter_shopitem_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="shopitem",
            name="date_created",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
