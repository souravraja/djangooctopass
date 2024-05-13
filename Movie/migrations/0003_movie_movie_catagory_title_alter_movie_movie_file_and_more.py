# Generated by Django 4.0 on 2024-05-07 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0002_movie_movie_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_catagory_title',
            field=models.CharField(choices=[('Popular', 'Popular Movie'), ('New-Movie', 'New Movie'), ('hollywood', 'hollywood Movie'), ('hindi', 'hindi Movie'), ('Bangoli', 'Bangoli Movie'), ('Hindi-Dub', 'Hindi Dub Movie')], default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_file',
            field=models.FileField(null=True, upload_to='movie/movieFile'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_title_image',
            field=models.ImageField(upload_to='movie/movieTitle'),
        ),
    ]
