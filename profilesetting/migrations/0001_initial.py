# Generated by Django 4.2.13 on 2024-06-25 07:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="SeeProfile",
            fields=[
                (
                    "id_user",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("bio", models.TextField(blank=True)),
                (
                    "profileimg",
                    models.ImageField(
                        blank=True,
                        default="https://images.pexels.com/photos/2416874/pexels-photo-2416874.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
                        null=True,
                        upload_to="profile_images",
                    ),
                ),
                ("location", models.CharField(blank=True, max_length=100)),
                ("mobilenumber", models.IntegerField(default=None)),
                (
                    "emailfield",
                    models.EmailField(blank=True, default=0, max_length=254, null=True),
                ),
                ("dob", models.DateField(blank=True, default=True, null=True)),
                (
                    "diolog",
                    models.CharField(
                        blank=True, default=True, max_length=500, null=True
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
