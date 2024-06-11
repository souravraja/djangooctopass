from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='socialmedia'),
    path('post_create_page',views.post_upload,name='post_create_page'),
    path('postdetail/<slug:post_slug>',views.postdetails,name='postdetails'),
    path('search/',views.searchUserPost,name='searchUserPost')
]