from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile

import random
# Create your views here.
def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['pswd']
        print(username)
        print(password)
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print('login succesfully')
            return redirect('/')
        else:
            print('inside else')
            messages.info(request,'credentials Invalid')
            return redirect('signin')
    else:
        print(' sign inout side else')
        return render(request,'userragistration/signin.html')

def signup(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['pswd']
        password2=request.POST['pswd2']
        print(username)
        print(email)
        print(password)
        print(password2)
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                #log user in and redirect to settings page
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                #create a Profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                # return redirect('settings')
                # return redirect('userragistration')
                print('sign up when profile save')
                return HttpResponseRedirect('./../settings/')

        else:
            messages.info(request, 'Password Not Matching')
            return redirect('signup')
    else:
        print('sign up outside else')
        return render(request,'userragistration/signup.html')

def profile_settings(request):
    # user_profile=Profile.objects.get(user=request.user)
    # if request.method == 'POST':
    #     print('post method.....................')
    #     if request.FILES.get('image') ==None:
    #         print('with image')
    #         image=user_profile.profileimg
    #         bio=request.POST['bio']
    #         location=request.POST['location']

    #         user_profile.profileimg=image
    #         user_profile.bio=bio
    #         user_profile.location=location
    #         user_profile.save()

    #     if request.FILES.get('image') !=None:
    #         print('with no image')
    #         image=request.FILES.get('image')
    #         bio=request.POST['bio']
    #         location=request.POST['location']

    #         user_profile.profileimg=image
    #         user_profile.bio=bio
    #         user_profile.location=location
    #         user_profile.save()
    #     return redirect('./../settings/')
    # else:
    #     print('get method..........')
        return render(request,'userragistration/profile_settings.html')
    

def prfile(request,pk):
    prfile=Profile.objects.get(id_user=pk)
    return render(request,'userragistration/profile.html',{'profile':prfile})