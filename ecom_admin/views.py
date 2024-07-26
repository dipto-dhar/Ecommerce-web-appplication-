from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import *
# from django.contrib.auth.models import User
from .models import User
from .models import *
from django.core.paginator import Paginator


def dashboard(request):
    if request.user.is_authenticated:
        return render(request,'admin_p/dashboard.html')
    else:
        if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']

            user=authenticate(request,username=username,password=password)
            if user is not None and user.groups.id is not 4:
                login(request,user)
                messages.success(request,'Successfully Logged In')
                return redirect('dashboard')
            else:
                messages.error(request,'Invalid Credential')
        return render(request,'admin_p/index.html')
        
def users(request):
    users= User.objects.all()
    return render(request,'admin_p/users.html',{'users':users})

def add_user(request):
    form=create_user()
    if request.method=='POST':
        form=create_user(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'User has been successfully added')
            return redirect('users')
    return render(request,'admin_p/add-user.html',{'form':form})

def categories(request):
    categories=Category.objects.all()
    return render(request,'admin_p/categories.html',{'categories':categories})

def add_category(request):
    form=create_category()
    if request.method=='POST' :
        form=create_category(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Category Created Successfully ')
            return redirect('categories')
    return render(request,'admin_p/add-category.html',{'form':form})

def edit_category(request,pk):
    object=Category.objects.get(id=pk)
    form=create_category(instance=object)
    if request.method=='POST':
        form=create_category(request.POST,request.FILES, instance=object)
        if form.is_valid():
            form.save()
            messages.success(request,'Category Updated Successfully')
            
    return render(request,'admin_p/edit-category.html',{'form':form})

def delete_category(request,pk):
    object=Category.objects.get(id=pk)
    object.delete()
    messages.success(request,'Category Deleted Successfully')
    return redirect('categories')

def add_product(request):
    form=create_product()
    if request.method=='POST' :
        form=create_product(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Product Created Successfully')
            return redirect('products')
    return render(request,'admin_p/add-product.html',{'form':form})

def products(request):
    products=Product.objects.order_by('-date')
    p=Paginator(products,20)
    p_no=request.GET.get('page')
    pages=p.get_page(p_no)
    total_pages=pages.paginator.num_pages
    

    return render(request,'admin_p/products.html',{'products':pages,'total_pages':[n+1 for n in range(total_pages) ] })

def edit_product(request,slug):
    object=Product.objects.get(slug=slug)
    form=create_product(instance=object)
    if request.method=='POST':
        form=create_product(request.POST,request.FILES, instance=object)
        if form.is_valid():
            form.save()
            messages.success(request,'Product Updated Successfully')
        
            
    return render(request,'admin_p/edit-product.html',{'form':form})

def delete_product(request,pk):
    object=Product.objects.get(id=pk)
    object.delete()
    messages.success(request,'Product Deleted Successfully')
    return redirect('products')