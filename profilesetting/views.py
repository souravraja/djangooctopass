from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Profile
from django.contrib.auth.decorators import login_required
import uuid
# Create your views here.
def signin(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['pswd']
        print(username)
        print(password)
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Crendentials Invalid')
            return redirect('signup')
    else:
        return render(request,'profilesetting/signin.html')

def signup(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        pswd=request.POST['pswd']
        pswd2=request.POST['pswd2']

        if pswd ==pswd2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'UserName Taken')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,email=email,password=pswd)
                user.save()
                print('raja1')
                # log user in and redirect to settings page 
                # create a Profile object for new user 
                user_model=User.objects.get(username=username)
                # print('raja2')
                new_profile=Profile.objects.create(user=user_model,id_user=user_model.id)
                print('raja3')
                new_profile.save()
                print('raja4')
                return redirect('signin')

        else:
            messages.info(request,'Pasword is not same')
            return redirect('signup')
        print(username)
        print(email)
        print(pswd)
        print(pswd2)
    else:
        return render(request,'profilesetting/signup.html')
    
@login_required(login_url='signin')
def profile(request,pk):
    user_profile=Profile.objects.get(user=request.user)
    print(user_profile.bio)
    return render(request,'profilesetting/profile.html',{'user_profile':user_profile})


@login_required(login_url='signin')
def logout(request):
    pass