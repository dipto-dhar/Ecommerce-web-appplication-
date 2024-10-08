from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from ecom_admin.models import User,Product
from .forms import register_user,update_user,update_password,shipping_info,contact_form
from ecom_admin.models import *
from .models import Cart, ShippingInfo, Order, OrderItem
from cart.context_processors import cart_summary
import json
import random
import string
import requests
from django.http import JsonResponse
# Create your views here.
from decimal import Decimal, InvalidOperation

def home(request):
    products=Product.objects.order_by('-date')
    categories=Category.objects.all()
    page_data=Homepage.objects.get(id=1)
    return render(request,'store/index.html',{'products':products,'categories':categories,'page':page_data})


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

def show_orders(request):
    if request.user.is_authenticated:
        
        orders= Order.objects.filter(user=request.user.id)
        order_items= OrderItem.objects.filter(user=request.user.id)

        return render(request, 'store/orders.html',{'orders':orders,'order_items':order_items})


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

def account_dashboard(request):
    return render(request, 'store/account_dashboard.html')
def checkout(request):
    headers = {
        'X-CSCAPI-KEY': 'd0FKT21PcEpLclVLakE4ZGRNczlFNnNTdVk1MUcxWTdIMFpGajZFcQ=='  # Your API Key
    }
    
    country_url = "https://api.countrystatecity.in/v1/countries"
    country_response = requests.get(country_url, headers=headers)
    countries = country_response.json()

    if request.session.get('cart'):
        if request.user.is_authenticated:
            try:
                user_shipping_info = ShippingInfo.objects.get(user=request.user)
                form = shipping_info(instance=user_shipping_info)
            except ShippingInfo.DoesNotExist:
                form = shipping_info()  # Empty form if no info exists
        else:
            form = shipping_info()

        return render(request, 'store/checkout.html', {'shipping_form': form, 'countries': countries})
    else:
        return redirect('404')

def cart(request):
    return render(request, 'store/cart.html')
def wishlist(request):
    return render(request, 'store/wishlist.html')


def contact(request):
    page_data=ContactPage.objects.get(id=1)
    form=contact_form()
    if request.method=='POST':
        form=contact_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Submited Successfully")
            return redirect("contact")
    return render(request,'store/contact.html',{'form':form,'page':page_data})

def about(request):
    page_data=AboutPage.objects.get(id=1)
   
    return render(request,'store/about.html',{'page':page_data})
def terms(request):
    page_data=TermsPage.objects.get(id=1)
   
    return render(request,'store/terms&condition.html',{'page':page_data})
def privacypolicy(request):
    page_data=PrivacyPolicyPage.objects.get(id=1)
   
    return render(request,'store/privacy.html',{'page':page_data})



def shipping_calc(request):
    headers = {
        'X-CSCAPI-KEY': 'd0FKT21PcEpLclVLakE4ZGRNczlFNnNTdVk1MUcxWTdIMFpGajZFcQ=='  # Your API Key
    }
    
    country_url = "https://api.countrystatecity.in/v1/countries"
    state_url = "https://api.countrystatecity.in/v1/states"
    

    # Fetch country data
    country_response = requests.get(country_url, headers=headers)
    countries = country_response.json()

    if request.method == 'POST' :
        action = request.POST.get('action')
        
        if action == 'get_states':
            country_id = request.POST.get('country_id')
            
            if country_id:

                state_response = requests.get(state_url, headers=headers)
                state_data = state_response.json()
            
                states = [state for state in state_data if state['country_code'] == country_id]
                
                return JsonResponse({'states': states})

        elif action == 'get_cities':

            state_code = request.POST.get('state_code')
            country_id = request.POST.get('country_id')
            
            if state_code:
                city_url = f"https://api.countrystatecity.in/v1/countries/{country_id}/states/{state_code}/cities"
                city_response = requests.get(city_url, headers=headers)
                cities_data = city_response.json()
               
                cities = [cities for cities in cities_data]

                return JsonResponse({'cities': cities})


def calculate_shipping(request):
    if request.method == 'POST':
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')  # Optional if using city
        total_price = Decimal(request.POST.get('total_price'))
        
        try:
            # Fetch the shipping zone based on country, state, and city
            shipping_zone = ShippingZone.objects.filter(
                country=country, state=state, city=city
            ).first()

            if shipping_zone:
                shipping_cost = shipping_zone.cost
                free_limit = shipping_zone.free_limit

                # Apply free shipping if cart total meets the free limit
                if total_price >= free_limit:
                    shipping_cost = 0

                return JsonResponse({
                    'success': True,
                    'shipping_cost': shipping_cost,
                    'total_price': total_price + shipping_cost
                })
            else:
                return JsonResponse({
                    'success': False,
                    'error': 'No shipping zone found for the selected region.'
                })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            })

    if request.method == 'POST':
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        print(country)
        print(state)
        print(city)
        
        # Find a shipping zone based on the country, state, and city
        try:
            shipping_zone = ShippingZone.objects.filter(
                country=country, state=state, city=city
            ).first()

            print(shipping_zone.cost)
            
            if shipping_zone:
                shipping_cost = shipping_zone.cost
                free_limit = shipping_zone.free_limit
                # Apply free shipping if the cart total meets the free limit
                total_price = Decimal(request.POST.get('total_price'))
                if total_price >= free_limit:
                    shipping_cost = 0

                return JsonResponse({
                    'success': True,
                    'shipping_cost': shipping_cost,
                    'total_price': total_price + shipping_cost
                })
            else:
                return JsonResponse({
                    'success': False,
                    'error': 'No shipping zone found for the selected region.'
                })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            })