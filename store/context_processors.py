from ecom_admin.models import *

def categories(request):
    products=Product.objects.order_by('-date')
    categories=Category.objects.all()
    
    return {'products':products,'categories':categories}