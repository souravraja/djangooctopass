from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        Number=request.POST['mumber']
        subject=request.POST['subject']
        message=request.POST['massage']
        print(name)
        print(email)
        print(subject)
        print(Number)
        print(message)
    return render(request,'eventotganizer/home.html')