from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email_address']
        Number=request.POST['phone']
        subject=request.POST['subject']
        message=request.POST['message']
        print(name)
        print(email)
        print(subject)
        print(Number)
        print(message)
    return render(request,'digitalbussiness/home.html')