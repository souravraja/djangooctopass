from django.contrib import admin
from .models import Student,Subject,Access_course,teacher,PlacementStory,catagory
# Register your models here.
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Access_course)
admin.site.register(teacher)
admin.site.register(catagory)
admin.site.register(PlacementStory)