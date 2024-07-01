from django.db import models
from django.core.validators import FileExtensionValidator 
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
language_choice=(
    ('ben','bengoli'),
    ('hindi','hindi'),
    ('English','English')
)
class classlanguage(models.Model):
    language=models.CharField(max_length=100,null=True,blank=True,default=None)
    def __str__(self):
        return self.language
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
    subject_language=models.ManyToManyField(classlanguage,blank=True,default=None,)
    catagory=models.ForeignKey(catagory,on_delete=models.CASCADE,default=None,blank=True,null=True)
    subject_price=models.IntegerField(default=None,blank=True,null=True)
    PDF = models.FileField(upload_to='education pdf file',null=True,  
                           blank=True,  
                           validators=[FileExtensionValidator( ['pdf'] ) ]) 
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

choice_status=(
    ('pending','pending'),
    ('accept','accept'),
    ('running','running'),
    ('fiensed','fiensed'),
)
class contectme(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    mob=models.IntegerField(max_length=13)
    email=models.EmailField(max_length=432)
    message=models.TextField()
    status=models.CharField(max_length=50,choices=choice_status,default='pending')