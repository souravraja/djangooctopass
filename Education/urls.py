from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='education'),
    path('course/',views.course,name='education_course'),
    path('course/<int:pk>',views.course,name='education_catagory_course'),
    path('catogory/',views.catogory,name='education_catogory'),
    path('contect/',views.contect,name='contect'),
    path('course_details/<int:pk>',views.course_details,name='course_details')
]