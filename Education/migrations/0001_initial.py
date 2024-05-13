# Generated by Django 4.0 on 2024-04-26 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('admition_date', models.DateField()),
                ('dob', models.DateField()),
                ('Teacher_img', models.ImageField(upload_to='education/student')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_img', models.ImageField(upload_to='education/subject')),
                ('subject_name', models.CharField(max_length=100)),
                ('subject_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('digree', models.TextField()),
                ('exprence', models.IntegerField()),
                ('Teacher_img', models.ImageField(upload_to='education/teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Access_course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subject_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Education.subject')),
                ('student_name', models.ManyToManyField(to='Education.Student')),
                ('techer_name', models.ManyToManyField(to='Education.teacher')),
            ],
        ),
    ]
