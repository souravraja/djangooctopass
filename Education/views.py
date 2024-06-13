from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'education/home.html')
    # return render(request,'fonthome/comedownpage.html')