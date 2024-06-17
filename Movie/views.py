from django.shortcuts import render
from .models import movie
from .forms import movieform,SearchMovieName
# Create your views here.
def moviehome(request):
    romanticmovie=movie.objects.filter(movie_type='Romance')
    poster=movie.objects.filter(movie_catagory_title='poster')
    popolarmovie=movie.objects.filter(movie_catagory_title='Popular')
    newmovie=movie.objects.filter(movie_catagory_title='New-Movie')
    hollywoodmovie=movie.objects.filter(movie_catagory_title='hollywood')
    hindimovie=movie.objects.filter(movie_catagory_title='hindi')
    bengolimovie=movie.objects.filter(movie_catagory_title='Bangoli')
    hindidubmovie=movie.objects.filter(movie_catagory_title='Hindi-Dub')
    if request.method=='post':
        print('post data')
        fm=SearchMovieName(request.POST)
        print('is out of valid')
        if fm.is_valid():
            print('is valid')
            print('name',fm.cleaned_data['nameofthemovie'])
    else:
        fm=SearchMovieName()
        print('get data1')
    return render(request,'movie/home.html',{'poster':poster,'popolarmovie':popolarmovie,
    'newmovie':newmovie,'hollywoodmovie':hollywoodmovie,'hindidubmovie':hindidubmovie,'benglimovie':bengolimovie,'hindimovie':hindimovie,'findmovie':fm})
    

def playmovie(request,pk):
    playmovie=movie.objects.get(pk=pk)
    return render(request,'movie/playmovie.html',{'playmovie':playmovie})  


def movies(request):
    allmovie=movie.objects.all()
    return render(request,'movie/movies.html',{'allmovie':allmovie})   


def trending(request):
    trend=movie.objects.filter(movie_select='trending')
    return render(request,'movie/trending.html',{'trend':trend})

def explore(request):
    explore=movie.objects.filter(movie_select='explore')
    return render(request,'movie/explore.html',{'explore':explore})

def favourite(request):
    favour=movie.objects.filter(movie_select='favourite')
    return render(request,'movie/favourite.html',{'favour':favour})


def movieuploadform(request):
    context={}
    form=movieform(request.POST,request.FILES)
    if form.is_valid():
        form.save()
    context['form']=form
    return render(request,'movie/form.html',context)

