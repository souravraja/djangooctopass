from django.shortcuts import render
from django.http import HttpResponse
from .models import Subject,Student,teacher,catagory
# Create your views here.
def home(request):
    subject=Subject.objects.order_by('?')[:6]
    Catagory=catagory.objects.order_by('?')[:6]

    context={'subject':subject,'cotagory':Catagory}
    return render(request,'education/home.html',context)
    # return render(request,'fonthome/comedownpage.html')

def course(request,pk=None):
    print(pk)
    if pk!=None:
        Catagory=catagory.objects.get(pk=pk)
        name=Catagory.catagory_name
        print(type(name))
        subject=Subject.objects.filter(catagory=Catagory)
        print(subject)
    else:
        subject=Subject.objects.all()
    context={'subject':subject}
    return render(request,'education/courses.html',context)


def catogory(request):
    Catagory=catagory.objects.all()
    context={'cotagory':Catagory}
    return render(request,'education/catagory.html',context)


def contect(request):
    # Catagory=catagory.objects.all()
    # context={'cotagory':Catagory}
    if request.method=="POST":
        print(request.POST)
        
    return render(request,'education/contact.html',)

def course_details(request,pk):
    subject=Subject.objects.get(pk=pk)
    return render(request,'education/course_details.html',{'subject':subject})