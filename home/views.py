from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup as bs
import requests
def home(request):
    if request.method=='POST':
        search=request.POST['search_box']
        print(search)
        url='https://www.ask.com/web?q='+search
        res=requests.get(url)
        soup=bs(res.text,'lxml')
        return render(request,'home/searchresult.html',{'su':soup})
    else:
        return render(request,'home/home.html')



# def searchresult(request):
    
    