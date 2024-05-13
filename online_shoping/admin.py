from django.contrib import admin
from .models import Cart,Customer,Product,OrderPlaced
# Register your models here.
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(OrderPlaced)