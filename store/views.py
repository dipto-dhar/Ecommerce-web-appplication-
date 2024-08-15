from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from ecom_admin.models import User,Product
from .forms import register_user,update_user,update_password,shipping_info
from ecom_admin.models import *
from .models import Cart, ShippingInfo, Order, OrderItem
from cart.context_processors import cart_summary
import json
import random
import string

# Create your views here.


def home(request):
    products=Product.objects.order_by('-date')
    categories=Category.objects.all()
    
    return render(request,'store/index.html',{'products':products,'categories':categories})


def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']

        user= authenticate(email=email,password=password)
        if user is not None:
            login(request,user)
            cart = request.session.get('cart', {})
            print(request.user.id)
            old_cart = Cart.objects.get(user_id=request.user.id)
            new_cart =old_cart.user_cart
            if new_cart:
                new_cart = json.loads(new_cart)
                request.session['cart'] = new_cart
                request.session.modified = True
            print(new_cart)

            return redirect('my-account')
            
            # user.update(cart=user_cart)
        else:
            pass
            return redirect('my-account')
        

    return render(request,'store/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def user_register(request):
    if request.user.is_authenticated:
        return redirect('home')
    form=register_user()
    if request.method=='POST':
        form=register_user(request.POST)
        if form.is_valid():
            form.save(commit=True)

            email=form.cleaned_data['email']
            password=form.cleaned_data['password1']
            user=authenticate(email=email,password=password)
            login(request,user)
                
            messages.success(request,'You have been registered successfully')
            return redirect('home')
    return render(request,'store/register.html',{'form':form})

def my_account(request):
    return render(request, 'store/my-account.html')


def user_update(request):
    if request.user.is_authenticated:
        user=request.user
        form=update_user(request.POST or None, instance=user)
        if request.method=='POST':
            if form.is_valid():
                    form.save()
                    messages.success(request,'Your account details has been updated successfully')
                

        return render(request,'store/update-user.html',{'update_form':form})
    else:
        return redirect("login")
    
def shippinginfo_update(request):
    if request.user.is_authenticated:
        user_shipping_info = ShippingInfo.objects.get(user__id=request.user.id)
        form = shipping_info(request.POST or None, instance=user_shipping_info)

        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'Your Shipping details have been updated successfully')
                return redirect('update_shipping')  

        return render(request, 'store/update-shipping.html', {'update_form': form})
    else:
        return redirect("login")
    

def process_order(request):

    def generate_unique_key():

        key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        return f'#{key}'            
    
    token=generate_unique_key()                        
    if request.session.get('cart'):
        if request.user.is_authenticated:

            
            if request.POST:
                user = request.user
                shipping_form = request.POST
                request.session['shipping_info'] = shipping_form
                shipping_info = request.session.get('shipping_info')
                full_name = shipping_info['name']
                phone = shipping_info['phone']
                email = shipping_info['email']
                total = cart_summary(request)['total_price']
                shipping_address = f"{shipping_info['address']}\n{shipping_info['city']}\n{shipping_info['zip_code']}\n{shipping_info['state']}"       
                place_order = Order(user=user,order_id=token, name=full_name, phone=phone, email=email, order_amount=total, shipping_address=shipping_address)
                place_order.save()

                order_id = place_order.pk
                print('Order ID:', order_id)

                cart_items = cart_summary(request)['cart_items']
                quantity = cart_summary(request)['qty']

                # Assuming 'quantity' is a dictionary where the key is product_id and value is quantity
                for item in cart_items:
                    product_id = item.id
                    price = item.sale_price if item.on_sale else item.regular_price

                    if str(product_id) in quantity:
                            product_qty = quantity[str(product_id)]
                    

                            # Create the order item
                            order_item = OrderItem(
                                user=user, 
                                order=place_order,  # Pass the order object directly, not the ID
                                product=item,  # Pass the product object directly
                                quantity=product_qty, 
                                price=price, 
                                total_price=product_qty * price
                            )
                            order_item.save()
                request.session['order']={'id':place_order.pk}
            
        
                
        else:

            if request.POST:
                
                    shipping_form = request.POST
                    request.session['shipping_info'] = shipping_form
                    shipping_info = request.session.get('shipping_info')
                    full_name = shipping_info['name']
                    phone = shipping_info['phone']
                    email = shipping_info['email']
                    total = cart_summary(request)['total_price']
                    shipping_address = f"{shipping_info['address']}\n{shipping_info['city']}\n{shipping_info['zip_code']}\n{shipping_info['state']}"       
                    place_order = Order(order_id=token, name=full_name, phone=phone, email=email, order_amount=total, shipping_address=shipping_address)
                    place_order.save()

                    order_id = place_order.pk
                    print('Order ID:', order_id)

                    cart_items = cart_summary(request)['cart_items']
                    quantity = cart_summary(request)['qty']

                    # Assuming 'quantity' is a dictionary where the key is product_id and value is quantity
                    for item in cart_items:
                        product_id = item.id
                        price = item.sale_price if item.on_sale else item.regular_price

                        if str(product_id) in quantity:
                                product_qty = quantity[str(product_id)]
                        

                                # Create the order item
                                order_item = OrderItem(
                                    order=place_order,  # Pass the order object directly, not the ID
                                    product=item,  # Pass the product object directly
                                    quantity=product_qty, 
                                    price=price, 
                                    total_price=product_qty * price
                                )
                                order_item.save()
                    request.session['order']={'id':place_order.pk}
        
        request.session.get('cart').clear()        
        return redirect('thank-you')
                             
    else:
        return redirect('404')          



def thank_you(request):
    if request.session.get('order'):
        order_id=request.session.get('order')['id']
        order= Order.objects.get(id=int(order_id))
        order_items= OrderItem.objects.filter(order=int(order_id))
        customer_name= ''
        customer_email= ''
        if request.user.is_authenticated:
            customer_name= request.user.first_name
            customer_email= request.user.email
        else:
            customer_name=request.session.get('shipping_info')['name']
            customer_name = customer_name.split()[0]

            customer_email=request.session.get('shipping_info')['email']
        print(order.name)
        return render(request, 'store/thank-you.html',{'customer_name':customer_name,'customer_email':customer_email,'order_total':order.order_amount,'order_token':order.order_id,'items':order_items})
           # Additional logic (e.g., clearing the cart) can go here
    else:
        return redirect('404')
        

        

    
def password_update(request):
    if request.user.is_authenticated:
        user=request.user
        form=update_password(user)
        
        if request.method == "POST":
            form=update_password(user,request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Your Password has been updated successfully')
                return render(request,'store/update-password.html',{'password_form':form})
        else:
            return render(request,'store/update-password.html',{'password_form':form})
    else:
        return redirect("login")
    

    

def shop(request):
        products=Product.objects.order_by('-date')
        return render(request, 'store/shop.html',{'products':products})
  
def page_not_found(request):
        return render(request, 'store/404.html')
  
def shop_by(request,slug):
        category=Category.objects.get(slug=slug)
        products=Product.objects.filter(category=category)
        return render(request, 'store/shop-by.html',{'products':products,'category':category})

def product(request,slug):
    product=Product.objects.get(slug=slug)
    return render(request, 'store/product.html',{'product':product})
def category(request):
    return render(request, 'store/category.html')
def checkout(request):
    if request.session.get('cart'):
        if request.user.is_authenticated:
            user_shipping_info = ShippingInfo.objects.get(user__id=request.user.id)
            form = shipping_info( instance=user_shipping_info)
        else:
            form = shipping_info()

        return render(request, 'store/checkout.html', {'shipping_form':form})
    else:
        return redirect('404')
def cart(request):
    return render(request, 'store/cart.html')
def wishlist(request):
    return render(request, 'store/wishlist.html')
def about(request):
    return render(request, 'store/about.html')
def contact(request):
    return render(request, 'store/contact.html')
