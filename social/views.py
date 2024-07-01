from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from .models import Post
from profilesetting.models import Profile
from .models import Post
from itertools import chain

# Create your views here.
def home(request):
    user_object=User.objects.get(username=request.user.username)
    # user_profile=Profile.objects.get(user=user_object)
    user_profile=Profile.objects.get(user=user_object)
    prfile=Profile.objects.get(user=request.user)
    print('user name is',user_object)
    print('user profile is',user_profile)
    print('user profile is',user_profile.bio)
    # return HttpResponse('hello')
    post=Post.objects.order_by("?")
    context={
        'post':post,
        'username':user_object,
        'userprofile':user_profile,
        'profile':prfile
        }
    return render(request,'social/home.html',context)
    

def postdetails(request,post_slug):
    postd=Post.objects.get(id=post_slug)
    print('postdetails')
    print(post_slug)
    return render(request,'social/postdetails.html',{'post':postd})

# @login_required(login_url='signin')
def post_upload(request):
    if request.method=='POST':
        user=request.user
        image=request.FILES.get('image_upload')
        posttext=request.POST['caption']
        print("ajj tak")
        print('image is',image)
        print('caption is',posttext)
        print(user)
        print('kal')
        new_post=Post.objects.create(user=user,image=image,caption=posttext)
        new_post.save()
        return redirect('/social/')
    else:
        return render(request,'social/post_create_form.html') 
    

def searchUserPost(request):
    user_object=User.objects.get(username=request.user.username)
    user_profile=Profile.objects.get(user=user_object)
    if request.method =='POST':
        username=request.POST['searchUsernamePost']
        username_object=User.objects.filter(username__icontains=username)
        print(username_object)
        username_profile=[]
        username_profile_list=[]
        for users in username_object:
            username_profile.append(users.id)

        for ids in username_profile:
            profle_lists=Profile.objects.filter(id_user=ids)
            username_profile_list.append(profle_lists)

        username_profile_list=list(chain(*username_profile_list))
        context={
            'user_prfile':user_profile,
            'username_profile_list':username_profile_list
        }
    return render(request,'social/search.html',context)