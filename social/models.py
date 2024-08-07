from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
import uuid
from datetime import datetime
from django.core.validators import FileExtensionValidator 

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='social_post_images',null=True,blank=True)
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class SocialStory(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='social_post_images',null=True,blank=True)
    text=models.CharField(max_length=100)
    video=models.FileField(upload_to='videos_uploaded',null=True,
validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])