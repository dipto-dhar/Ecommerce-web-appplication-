from django.shortcuts import render,redirect,HttpResponse





def cart_summary(request):
    return render(request,'store/cart.html')

def add_to_cart(request):
    pass

def update_cart(request):
    pass

def delete_from_cart(request):
    pass
