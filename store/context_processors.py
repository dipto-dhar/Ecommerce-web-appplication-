from ecom_admin.models import *
from .models import *

def categories(request):
    products=Product.objects.order_by('-date')
    categories=Category.objects.all()
    
    return {'products':products,'categories':categories}


def store_info(request):
    store_info = Settings.objects.first()

    return {'store':store_info}

def order_count(request):
    new_order= Order.objects.filter(status=1)
    new_order_count= len(new_order)
    print(new_order_count)
    return {'new_order':new_order_count}
