from django.shortcuts import render,redirect,HttpResponse, get_object_or_404
from .cart import Cart
from ecom_admin.models import Product
from django.http import JsonResponse





def cart_summary(request):
    return render(request,'store/cart.html')

def add_to_cart(request):
    cart = Cart(request)

    if request.POST.get('action')=='post':
        product_id = int(request.POST.get('product_id'))

        product= get_object_or_404(Product, id=product_id)

        cart.add(product=product)
        response= JsonResponse({'Product Name': product.name})
        return response

def update_cart(request):
    pass

def delete_from_cart(request):
    pass
