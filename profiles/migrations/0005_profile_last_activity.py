# Generated by Django 5.0.6 on 2024-06-01 16:46

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0004_alter_profile_thumbnail"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="last_activity",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
