# Generated by Django 4.0 on 2024-04-21 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_shoping', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='descrption',
            field=models.TextField(default=0),
        ),
    ]
