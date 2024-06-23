from django.db import models
from django.contrib.auth import get_user_model
import uuid
User=get_user_model()
# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False) 
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='https://images.pexels.com/photos/2416874/pexels-photo-2416874.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',blank=True,null=True)
    location = models.CharField(max_length=100, blank=True)
    mobilenumber=models.IntegerField(default=None)
    emailfield=models.EmailField(default=0,null=True,blank=True)
    dob=models.DateField(default=True,null=True,blank=True)

    def __str__(self):
        return self.user.username
