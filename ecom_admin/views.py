from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import *
# from django.contrib.auth.models import User
from .models import User
from .models import *
from store.models import *
from django.core.paginator import Paginator
from .restriction import authenticated_user
import requests
from django.http import JsonResponse

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


@authenticated_user(allowed_roles=['Admin','Super Admin','Editor'])
def users(request):
    users= User.objects.all()
    return render(request,'admin_p/users.html',{'users':users})

@authenticated_user(allowed_roles=['Admin','Super Admin'])
def add_user(request):
    form=create_user()
    if request.method=='POST':
        form=create_user(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'User has been successfully added')
            return redirect('users')
    return render(request,'admin_p/add-user.html',{'form':form})

@authenticated_user(allowed_roles=['Super Admin'])
def edit_user(request,pk):
    user=User.objects.get(id=pk)
    form=edit_user_form(instance=user)
    if request.method=='POST':
        form=edit_user_form(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,'User has been successfully added')
            return redirect('users')
    return render(request,'admin_p/edit-user.html',{'form':form,'user':user})
@authenticated_user(allowed_roles=['Super Admin'])
def delete_user(request,pk):
    user=User.objects.get(id=pk)
    user.delete()
    return redirect('users')
@authenticated_user(allowed_roles=['Admin','Super Admin','Editor'])
def contacts(request):
    contacts_list = Contacts.objects.all()

    # Handle search functionality
    query = request.GET.get('q')
    if query:
        contacts_list = contacts_list.filter(name__icontains=query)

    # Pagination: Show 7 contacts per page
    paginator = Paginator(contacts_list, 7)  # 7 contacts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'contacts': page_obj,  # Pass the paginated contacts
    }
    return render(request, 'admin_p/contacts.html', context)

# View to handle deleting a contact
def delete_contact(request, pk):
    contact = Contacts.objects.get(id=pk)

    if request.method == 'POST':
        contact.delete()
        messages.success(request, 'Contact deleted successfully.')
        return redirect('contacts')  # Redirect back to the contact list page after deletion

    return redirect('contacts')

@authenticated_user(allowed_roles=['Admin','Super Admin','Editor'])
def categories(request):
    categories=Category.objects.all()
    return render(request,'admin_p/categories.html',{'categories':categories})

@authenticated_user(allowed_roles=['Admin','Super Admin','Editor'])
def add_category(request):
    form=create_category()
    if request.method=='POST' :
        form=create_category(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Category Created Successfully ')
            return redirect('categories')
    return render(request,'admin_p/add-category.html',{'form':form})


@authenticated_user(allowed_roles=['Admin','Super Admin','Editor'])
def edit_category(request,pk):
    object=Category.objects.get(id=pk)
    form=create_category(instance=object)
    if request.method=='POST':
        form=create_category(request.POST,request.FILES, instance=object)
        if form.is_valid():
            form.save()
            messages.success(request,'Category Updated Successfully')
            
    return render(request,'admin_p/edit-category.html',{'form':form})
    

@authenticated_user(allowed_roles=['Admin','Super Admin'])
def delete_category(request,pk):
    object=Category.objects.get(id=pk)
    object.delete()
    messages.success(request,'Category Deleted Successfully')
    return redirect('categories')

@authenticated_user(allowed_roles=['Admin','Super Admin','Editor'])
def add_product(request):
    form=create_product()
    if request.method=='POST' :
        form=create_product(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Product Created Successfully')
            return redirect('products')
    return render(request,'admin_p/add-product.html',{'form':form})

@authenticated_user(allowed_roles=['Admin','Super Admin','Editor'])
def products(request):
    products=Product.objects.order_by('-date')
    p=Paginator(products,20)
    p_no=request.GET.get('page')
    pages=p.get_page(p_no)
    total_pages=pages.paginator.num_pages
    

    return render(request,'admin_p/products.html',{'products':pages,'total_pages':[n+1 for n in range(total_pages) ] })

@authenticated_user(allowed_roles=['Admin','Super Admin','Editor'])
def edit_product(request,slug):
    object=Product.objects.get(slug=slug)
    form=create_product(instance=object)
    if request.method=='POST':
        form=create_product(request.POST,request.FILES, instance=object)
        if form.is_valid():
            form.save()
            messages.success(request,'Product Updated Successfully')
        
            
    return render(request,'admin_p/edit-product.html',{'form':form})

@authenticated_user(allowed_roles=['Admin','Super Admin'])
def delete_product(request,pk):
    object=Product.objects.get(id=pk)
    object.delete()
    messages.success(request,'Product Deleted Successfully')
    return redirect('products')

@authenticated_user(allowed_roles=['Admin','Super Admin'])
def bulk_delete(request):
    if request.method == 'POST':
        # Get the list of IDs from the submitted form
        selected_item = request.POST.getlist('selected_ids')
        # Delete the selected objects
        Product.objects.filter(id__in=selected_item).delete()
        return redirect('products')  # Replace with your actual redirect URL


@authenticated_user(allowed_roles=['Admin','Super Admin','Editor'])
def orders(request):
    orders= Order.objects.all().order_by('-date')
    return render(request,'admin_p/orders.html',{'orders':orders})


@authenticated_user(allowed_roles=['Admin','Super Admin','Editor'])
def single_order(request, order_id):
    order= Order.objects.get(order_id=order_id)
    order_item= OrderItem.objects.filter(order=order)

    order_status=OrderStatus.objects.get(order=order)
    
    form= update_order_status_form(instance=order_status)
    if request.method=='POST':
        form=update_order_status_form(request.POST ,instance=order)
        if form.is_valid:
            form.save()
    else:
        form= update_order_status_form(instance=order_status)

    return render(request,'admin_p/single-order.html',{'order':order, 'order_items':order_item, 'form':form})

    


@authenticated_user(allowed_roles=['Admin','Super Admin'])
def delete_order(request, order_id):
    order= Order.objects.get(order_id=order_id)
    order.delete()
    return redirect('orders')
@authenticated_user(allowed_roles=['Admin','Super Admin','Editor'])
def update_order_status(request):
    form= update_order_status_form()
    if request.method=='POST':
        form=update_order_status_form(request.POST)
        if form.is_valid:
            form.save()
    else:
        form= update_order_status_form()
    
    return render(request, 'status.html',{'form':form})
@authenticated_user(allowed_roles=['Admin','Super Admin','Editor'])
def update_homepage(request):
    instance=Homepage.objects.get(id=1)
    form=HomepageForm(instance=instance)

    if request.method=='POST':
        form=HomepageForm(request.POST,request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request,'Homepage Updated Successfully')
        else:
            messages.success(request,'Error Updating tha Page')

    return render(request,'admin_p/pages/home.html',{'form':form})
@authenticated_user(allowed_roles=['Admin','Super Admin','Editor'])
def update_aboutpage(request):
    instance=AboutPage.objects.get(id=1)
    form=AboutPageForm(instance=instance)

    if request.method=='POST':
        form=AboutPageForm(request.POST,request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request,'About page Updated Successfully')
        else:
            messages.success(request,'Error Updating tha Page')

    return render(request,'admin_p/pages/about.html',{'form':form})
@authenticated_user(allowed_roles=['Admin','Super Admin','Editor'])
def update_contactpage(request):
    instance=ContactPage.objects.get(id=1)
    form=ContactPageForm(instance=instance)

    if request.method=='POST':
        form=ContactPageForm(request.POST,request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request,'Contact page Updated Successfully')
        else:
            messages.success(request,'Error Updating tha Page')

    return render(request,'admin_p/pages/contact.html',{'form':form})



@authenticated_user(allowed_roles=['Admin','Super Admin','Editor'])
def update_termspage(request):
    instance=TermsPage.objects.get(id=1)
    form=TermsPageForm(instance=instance)

    if request.method=='POST':
        form=TermsPageForm(request.POST,request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request,'Terms & Condition page Updated Successfully')
        else:
            messages.success(request,'Error Updating tha Page')

    return render(request,'admin_p/pages/terms.html',{'form':form})

@authenticated_user(allowed_roles=['Admin','Super Admin','Editor'])
def update_privacypage(request):
    instance=PrivacyPolicyPage.objects.get(id=1)
    form=PrivacyPolicyPageForm(instance=instance)

    if request.method=='POST':
        form=PrivacyPolicyPageForm(request.POST,request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request,'Privacy Policy page Updated Successfully')
        else:
            messages.success(request,'Error Updating tha Page')

    
    
    
    

    return render(request,'admin_p/pages/privacy-policy.html',{'form':form})


@authenticated_user(allowed_roles=['Admin','Super Admin','Editor'])
def shipping_zones(request):
    shipping_zones = ShippingZone.objects.all()
    paginator = Paginator(shipping_zones, 10)  # Show 10 shipping zones per page
    page_number = request.GET.get('page')
    zones = paginator.get_page(page_number)
    
    total_pages = range(1, paginator.num_pages + 1)

    return render(request, 'admin_p/shipping_zones.html', {
        'shipping_zones': zones, 
        'total_pages': total_pages
    })

@authenticated_user(allowed_roles=['Admin','Super Admin','Editor'])
def delete_shipping_zone(request, zone_id):
    # Get the shipping zone by id or return a 404 error if not found
    zone = ShippingZone.objects.get(id=zone_id)


        # Delete the shipping zone
    zone.delete()
    messages.success(request, "Shipping Zone deleted successfully.")
    
    return redirect('shipping-zones')  # Redirect to the list page after deletion
    

@authenticated_user(allowed_roles=['Admin','Super Admin','Editor'])
def add_shipping_zone(request):

    if request.method == 'POST':
        country_id = request.POST.get('country_id')
        state_code = request.POST.get('state_code')
        city = request.POST.get('city')
        action = request.POST.get('action')

        if action == 'get_shipping_price':
            shipping_cost = ShippingZone.get_shipping_cost(country_id, state_code, city)
            return JsonResponse({'shipping_cost': shipping_cost})
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
                print(cities_data)
                cities = [cities for cities in cities_data]

                return JsonResponse({'cities': cities})
    
    
    return render(request, 'admin_p/shipping.html', {'countries': countries})

@authenticated_user(allowed_roles=['Admin','Super Admin','Editor'])
def shipping_zone_submit(request):

    if request.method == 'POST' :
        country=request.POST.get('country')
        name=request.POST.get('zone_name')
        state=request.POST.get('state')
        city=request.POST.get('city')
        method=request.POST.get('method')
        cost=request.POST.get('cost')
        free_limit=request.POST.get('free_limit')


        form = ShippingZone(
            name=name,
            country=country,
            state=state,
            city=city,
            method=method,
            cost=cost,
            free_limit=free_limit
        )
        form.save()

        return redirect('shipping-zones')


@authenticated_user(allowed_roles=['Admin','Super Admin'])
def settings(request):
    settings = Settings.objects.first()
    if not settings:
        settings = Settings.objects.create(
            site_name='My E-commerce Site',
            site_tagline='Best products available',
            site_description='Welcome to our e-commerce platform.',
            store_address='1234 Market Street, City, Country',
            contact_email='contact@example.com',
            admin_email='admin@example.com',
            phone_number='123-456-7890',
            store_country='USA',
            store_currency='USD',
            meta_title='My E-commerce Site',
            meta_description='Buy the best products at the best prices.',
        )
    
    if request.method == 'POST':
        form = SettingsForm(request.POST, request.FILES, instance=settings)
        if form.is_valid():
            form.save()
            messages.success(request, 'Settings updated successfully!')
            return redirect('settings')  # Ensure 'settings' is the name of your URL pattern
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SettingsForm(instance=settings)
    
    return render(request, 'admin_p/settings.html', {'settings': settings, 'form': form})