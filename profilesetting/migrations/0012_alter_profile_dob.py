# Generated by Django 4.2.13 on 2024-07-01 01:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profilesetting", "0011_alter_profile_dob"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="dob",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(
                    2024, 7, 31, 1, 39, 41, 144671, tzinfo=datetime.timezone.utc
                ),
                null=True,
            ),
        ),
    ]