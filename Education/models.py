from django.db import models

# Create your models here.


class teacher(models.Model):
    name=models.CharField(max_length=1000)
    digree=models.TextField(blank=True,default=None,null=True)
    exprence=models.IntegerField(blank=True,default=None,null=True)
    Teacher_img=models.ImageField(upload_to='education/teacher',blank=True,default=None,null=True)
    Teacher_mobile_nnumber=models.CharField(max_length=12,blank=True,null=True,default=None)
    Teacher_alternative_mobile_nnumber=models.CharField(max_length=12,blank=True,null=True,default=None)
    Teacher_email=models.EmailField(max_length=912,blank=True,null=True,default=None)
    def __str__(self):
        return self.name

class Student(models.Model):
    name=models.CharField(max_length=200)
    address=models.TextField(blank=True,null=True,default=None)
    admition_date=models.DateField(blank=True,null=True,default=None)
    dob=models.DateField(blank=True,null=True,default=None)
    Student_img=models.ImageField(upload_to='education/student',blank=True,null=True,default=None)
    student_mobile_nnumber=models.CharField(max_length=12,blank=True,null=True,default=None)
    student_alternative_mobile_nnumber=models.CharField(max_length=12,blank=True,null=True,default=None)
    student_email=models.EmailField(max_length=912,blank=True,null=True,default=None)
    def __str__(self):
        return self.name

class catagory(models.Model):
    catagory_icon=models.ImageField(upload_to='catagoryicon',blank=True,default=None,null=True)
    catagory_name=models.CharField(max_length=100,default=None,null=True,blank=True)
    catagory_Descriptin=models.CharField(max_length=100,default=None,null=True,blank=True)
    def __str__(self):
        return self.catagory_name

class Subject(models.Model):
    subject_img=models.ImageField(upload_to='education/subject',blank=True,default=None,null=True)
    subject_name=models.CharField(max_length=100,blank=True,default=None,null=True)
    subject_description=models.TextField(blank=True,default=None,null=True)
    subject_duration=models.CharField(max_length=1000,blank=True,default=None,null=True)
    subject_language=models.CharField(max_length=2000,blank=True,default=None,null=True)
    catagory=models.ForeignKey(catagory,on_delete=models.CASCADE,default=None,blank=True,null=True)
    subject_price=models.IntegerField(default=None,blank=True,null=True)
    subject_syllybas=models.FileField(upload_to='education pdf file',default=None,blank=True,null=True)
    def __str__(self):
        return self.subject_name


class Access_course(models.Model):
    Subject_name=models.ForeignKey(Subject,on_delete=models.CASCADE)
    techer_name=models.ManyToManyField(teacher)
    student_name=models.ManyToManyField(Student)
    def __str__(self):
        return self.Subject_name
    

class PlacementStory(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    his_opinion=models.CharField(max_length=3000,blank=True,default=None,null=True)
    his_placement_company=models.CharField(max_length=500,blank=True,default=None,null=True)
