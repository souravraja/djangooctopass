from django.shortcuts import render
from .models import Product,Cart,Customer
# Create your views here.
def home(request):
    mobile=Product.objects.filter(category='MOB')
    laptop=Product.objects.filter(category='LaPTOP')
    shitr=Product.objects.filter(category='shitr')
    return render(request,'online_shoping/home.html',{'mobile':mobile,'laptop':laptop,'shitr':shitr})



def product_detail(request,pk):
    
    product_detels=Product.objects.get(pk=pk)
    return render(request,'online_shoping/porduct_detail.html',{'product_detail':product_detels})




def add_to_cart(request,pk):
    user=request.user
    product=Product.objects.get(id=pk)
    Cart(user=user,Product=product).save()
    
    print(user)
    return render(request,'online_shoping/cart.html')
   
def show_cart(request):
    if request.user.is_authenticated:
        user=request.user
        print(user)
        cart=Cart.objects.filter(user=user)
        amount=0
        totalprice=0.0
        shipping_amount=70
        total_amount=0
        cart_product=[p for p in Cart.objects.all() if p.user==user]
        print(cart_product)
        if cart_product:
            for amount in cart_product:
                tempamount=(amount.quantity*amount.Product.discounted_price)
                totalprice=totalprice+tempamount
                total_amount = totalprice+shipping_amount
            return render(request,'online_shoping/cart.html',{'carts':cart,'totalamount':total_amount,'amount':totalprice})
        else:
            return render(request,'online_shoping/empty-cart.html')
        



def checkout(request):
    user=request.user
    addrs=Customer.objects.filter(user=user)
    cart_items=Cart.objects.filter(user=user)
    amount=0.0
    shippig_amount=70.0
    totalamount=0.0
    cart_produnt=[p for p in Cart.objects.all() if p.user==request.user]
    if cart_produnt:
        for p in cart_produnt:
            tempamount=(p.quantity*p.Product.discounted_price)
            amount += tempamount
        totalamount=amount+shippig_amount
        return render(request,'online_shoping/checkout.html',{'address':addrs,'totalamount':totalamount,'cart_items':cart_items})