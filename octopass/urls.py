"""octopass URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls'),name=''),
    path('booking/',include('booking.urls'),name='booking'),
    path('doctor/',include('doctor.urls'),name='doctor'),
    # path('libriry/',include('library.urls'),name='libriry'),
    path('matrimonial/',include('matrimonial.urls'),name='matrimonial'),
    path('Movie/',include('Movie.urls'),name='Movie'),
    path('news/',include('news.urls'),name='news'),
    path('online_bank/',include('online_bank.urls'),name='online_bank'),
    path('online_shoping/',include('online_shoping.urls'),name='online_shoping'),
    path('ownshop/',include('ownshop.urls'),name='ownshop'),
    path('parlour/',include('parlour.urls'),name='parlour'),
    path('profilesetting/',include('profilesetting.urls'),name='profilesetting'),
    path('rent/',include('rent.urls'),name='rent'),
    path('social/',include('social.urls'),name='Socialmedia'),
    path('translator/',include('translator.urls'),name='translator'),
    path('reviewhomepage/',include('review.urls'),name='reviewhomepage'),
    path('digitalBussiness/',include('digitalBussiness.urls'),name='digitalbussiness'),
    path('Education/',include('Education.urls'),name='education'),
    path('eventOrganizer/',include('eventOrganizer.urls'),name='eventorganizer'),
    path('realState/',include('realState.urls'),name='realstate'),
]
urlpatterns = urlpatterns+static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)