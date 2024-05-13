from django.db import models

# Create your models here.


class teacher(models.Model):
    name=models.CharField(max_length=1000)
    digree=models.TextField()
    exprence=models.IntegerField()
    Teacher_img=models.ImageField(upload_to='education/teacher')
    def __str__(self):
        return self.name

class Student(models.Model):
    name=models.CharField(max_length=200)
    address=models.TextField()
    admition_date=models.DateField()
    dob=models.DateField()
    Teacher_img=models.ImageField(upload_to='education/student')
    def __str__(self):
        return self.name


class Subject(models.Model):
    subject_img=models.ImageField(upload_to='education/subject')
    subject_name=models.CharField(max_length=100)
    subject_description=models.TextField()
    def __str__(self):
        return self.subject_name


class Access_course(models.Model):
    Subject_name=models.ForeignKey(Subject,on_delete=models.CASCADE)
    techer_name=models.ManyToManyField(teacher)
    student_name=models.ManyToManyField(Student)
    def __str__(self):
        return self.id