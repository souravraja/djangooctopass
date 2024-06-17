from django.urls import path
from . import views
urlpatterns = [
    path('',views.moviehome,name='movie'),
    path('movies/',views.movies,name='movies'),
    path('playmovie/<int:pk>',views.playmovie,name='playmovie'),
    path('explore/',views.explore,name='explore'),
    path('trending/',views.trending,name='trending'),
    path('favourite/',views.favourite,name='favourite'),
    path('movieuplode/',views.movieuploadform,name='movieupload')
    # path('playmovie',views.playmovie,name='playmovie')
]