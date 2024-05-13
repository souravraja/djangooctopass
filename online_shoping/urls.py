from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='online_shoping_home'),
    path('product-detail/<int:pk>',views.product_detail,name='product-detail'),
    path('add-to-cart/<int:pk>',views.add_to_cart,name='add_to_cart'),
    path('show-card',views.show_cart,name='show-card'),
    path('check_out',views.checkout,name='check_out')
]