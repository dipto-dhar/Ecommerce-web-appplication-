from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from ecom_admin.models import User 
from .forms import register_user
from ecom_admin.models import *


# Create your views here.


def home(request):
    products=Product.objects.order_by('-date')
    categories=Category.objects.all()
    
    return render(request,'store/index.html',{'products':products,'categories':categories})
def base(request):

    categories=Category.objects.all()
    
    return render(request,'store/base.html',{'categories':categories})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']

        user= authenticate(email=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')

    return render(request,'store/login.html')

def user_logout(request):
    logout(request)
    return redirect('home')

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

def shop(request):
        products=Product.objects.order_by('-date')
        return render(request, 'store/shop.html',{'products':products})
  
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
    return render(request, 'store/checkout.html')
def cart(request):
    return render(request, 'store/cart.html')
def wishlist(request):
    return render(request, 'store/wishlist.html')
def about(request):
    return render(request, 'store/about.html')
def contact(request):
    return render(request, 'store/contact.html')
def my_account(request):
    return render(request, 'store/my-account.html')

