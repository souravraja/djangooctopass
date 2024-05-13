from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from .models import Post
from userragistration.models import Profile
# Create your views here.
def home(request):
    user_object=User.objects.get(username=request.user.username)
    # user_profile=Profile.objects.get(user=user_object)
    print('user name is',user_object)
    # print('user profile is',user_profile)
    return render(request,'social/home.html')


# @login_required(login_url='signin')
def post_upload(request):
    if request.method=='POST':
        user=request.user
        image=request.FILES.get('image_upload')
        posttext=request.POST['caption']
        print(posttext)
        print(user)
        new_post=Post.objects.create(user=user,image=image,caption=posttext)
        new_post.save()
        return redirect('/')
    else:
        return render(request,'social/post_create_form.html') 