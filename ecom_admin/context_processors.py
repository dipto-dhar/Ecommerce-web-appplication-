from .models import Settings
from store.models import Order

def store_info(request):
    store_info = Settings.objects.first()

    return {'store':store_info}

def order_count(request):
    new_order= Order.objects.filter(status=1)
    new_order_count= len(new_order)
    print(new_order_count)
    return {'new_order':new_order_count}

