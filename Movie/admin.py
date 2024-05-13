from django.contrib import admin
from .models import movie
# Register your models here.
@admin.register(movie)
class movieList(admin.ModelAdmin):
    list_display=('movie_name','movie_catagory_title','movie_type')
